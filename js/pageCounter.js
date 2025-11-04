// Page View Counter for coaiexist.wtf
// Uses Supabase as real backend storage

(function() {
  const SUPABASE_URL = 'https://aqxrogaltuwtlparwdkq.supabase.co';
  const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFxeHJvZ2FsdHV3dGxwYXJ3ZGtxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxMDY0NzAsImV4cCI6MjA3NzY4MjQ3MH0.qvkQaoQa7MaN7drGHKGxU3c1KnTQOdTH022MynR6fzI';

  async function initCounter() {
    const pagePath = location.pathname || '/';

    // Wait a bit for nav to load (if it's being fetched)
    await new Promise(resolve => setTimeout(resolve, 200));

    const counterEl = document.getElementById('page-counter');
    if (!counterEl) {
      console.log('Counter element not found');
      return;
    }

    try {
      // Get current count from Supabase
      const getRes = await fetch(
        `${SUPABASE_URL}/rest/v1/page_views?page_path=eq.${encodeURIComponent(pagePath)}`,
        {
          headers: {
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${SUPABASE_KEY}`
          }
        }
      );

      if (!getRes.ok) {
        throw new Error('Failed to fetch count');
      }

      const data = await getRes.json();
      let count = 0;

      // Check if this is a new visit (per session)
      const sessionKey = 'viewed_' + pagePath;
      const shouldIncrement = !sessionStorage.getItem(sessionKey);

      if (data.length === 0) {
        // No entry exists yet - create it
        count = 1;

        const createRes = await fetch(
          `${SUPABASE_URL}/rest/v1/page_views`,
          {
            method: 'POST',
            headers: {
              'apikey': SUPABASE_KEY,
              'Authorization': `Bearer ${SUPABASE_KEY}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              page_path: pagePath,
              view_count: count
            })
          }
        );

        if (!createRes.ok) {
          throw new Error('Failed to create count');
        }

        sessionStorage.setItem(sessionKey, 'true');

      } else {
        // Entry exists
        count = data[0].view_count;

        if (shouldIncrement) {
          // Increment the count
          count++;

          const updateRes = await fetch(
            `${SUPABASE_URL}/rest/v1/page_views?page_path=eq.${encodeURIComponent(pagePath)}`,
            {
              method: 'PATCH',
              headers: {
                'apikey': SUPABASE_KEY,
                'Authorization': `Bearer ${SUPABASE_KEY}`,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                view_count: count,
                last_updated: new Date().toISOString()
              })
            }
          );

          if (!updateRes.ok) {
            throw new Error('Failed to update count');
          }

          sessionStorage.setItem(sessionKey, 'true');
        }
      }

      // Display the count
      counterEl.textContent = '👁️ Views: ' + count;

    } catch (error) {
      console.error('Counter error:', error);
      counterEl.textContent = '👁️ N/A';
    }
  }

  // Auto-run when page loads
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCounter);
  } else {
    initCounter();
  }
})();
