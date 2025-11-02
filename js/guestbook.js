// Guestbook Widget for coaiexist.wtf
// Uses Supabase as backend storage

class Guestbook {
  constructor(containerId = 'guestbook-container') {
    this.containerId = containerId;
    this.maxNameLength = 50;
    this.maxMessageLength = 500;

    // Supabase configuration
    this.supabaseUrl = 'https://aqxrogaltuwtlparwdkq.supabase.co';
    this.supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFxeHJvZ2FsdHV3dGxwYXJ3ZGtxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIxMDY0NzAsImV4cCI6MjA3NzY4MjQ3MH0.qvkQaoQa7MaN7drGHKGxU3c1KnTQOdTH022MynR6fzI';
  }

  // Initialize and render the guestbook
  async init() {
    const container = document.getElementById(this.containerId);
    if (!container) {
      console.error('Guestbook container not found:', this.containerId);
      return;
    }

    // Load entries from Supabase
    const entries = await this.loadEntries();

    // Render UI
    container.innerHTML = this.renderUI(entries);

    // Attach event listeners
    this.attachEventListeners();
  }

  // Load guestbook entries from Supabase
  async loadEntries() {
    try {
      const response = await fetch(
        `${this.supabaseUrl}/rest/v1/guestbook_entries?approved=eq.true&order=created_at.desc`,
        {
          headers: {
            'apikey': this.supabaseKey,
            'Authorization': `Bearer ${this.supabaseKey}`
          }
        }
      );

      if (!response.ok) {
        throw new Error('Failed to load entries');
      }

      const entries = await response.json();
      return entries;
    } catch (error) {
      console.error('Error loading guestbook entries:', error);
      return [];
    }
  }

  // Render the complete guestbook UI
  renderUI(entries) {
    return `
      <div class="guestbook-widget">
        ${this.renderForm()}
        ${this.renderStats(entries)}
        ${this.renderEntries(entries)}
      </div>
    `;
  }

  // Render the sign form
  renderForm() {
    return `
      <div class="guestbook-form">
        <h3>Sign the Guestbook</h3>
        <form id="guestbook-sign-form">
          <div class="form-group">
            <label for="gb-name">Name:</label>
            <input
              type="text"
              id="gb-name"
              name="name"
              maxlength="${this.maxNameLength}"
              required
              placeholder="Your name or handle"
            />
          </div>
          <div class="form-group">
            <label for="gb-message">Message:</label>
            <textarea
              id="gb-message"
              name="message"
              maxlength="${this.maxMessageLength}"
              rows="4"
              required
              placeholder="Leave your mark on the digital cosmos..."
            ></textarea>
            <div class="char-counter">
              <span id="char-count">0</span>/${this.maxMessageLength}
            </div>
          </div>
          <div class="form-group">
            <label for="gb-website">Website (optional):</label>
            <input
              type="url"
              id="gb-website"
              name="website"
              placeholder="https://your-site.com"
            />
          </div>
          <button type="submit" class="sign-button">Sign Guestbook</button>
          <div id="form-status" class="form-status"></div>
        </form>
      </div>
    `;
  }

  // Render stats
  renderStats(entries) {
    return `
      <div class="guestbook-stats">
        <span class="stat-item">📝 Total Signatures: ${entries.length}</span>
      </div>
    `;
  }

  // Render entries list
  renderEntries(entries) {
    if (entries.length === 0) {
      return `
        <div class="guestbook-entries">
          <p class="no-entries">No entries yet. Be the first to sign!</p>
        </div>
      `;
    }

    const entriesHtml = entries.map(entry => this.renderEntry(entry)).join('');

    return `
      <div class="guestbook-entries">
        <h3>Signatures</h3>
        ${entriesHtml}
      </div>
    `;
  }

  // Render single entry
  renderEntry(entry) {
    const date = new Date(entry.created_at);
    const formattedDate = date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });

    const websiteLink = entry.website
      ? `<a href="${this.escapeHtml(entry.website)}" target="_blank" rel="noopener noreferrer" class="entry-website">🔗</a>`
      : '';

    return `
      <div class="guestbook-entry">
        <div class="entry-header">
          <span class="entry-name">${this.escapeHtml(entry.name)}</span>
          ${websiteLink}
          <span class="entry-date">${formattedDate}</span>
        </div>
        <div class="entry-message">${this.escapeHtml(entry.message)}</div>
      </div>
    `;
  }

  // Attach event listeners
  attachEventListeners() {
    const form = document.getElementById('guestbook-sign-form');
    const messageInput = document.getElementById('gb-message');
    const charCount = document.getElementById('char-count');

    if (form) {
      form.addEventListener('submit', (e) => this.handleSubmit(e));
    }

    if (messageInput && charCount) {
      messageInput.addEventListener('input', (e) => {
        charCount.textContent = e.target.value.length;
      });
    }
  }

  // Handle form submission
  async handleSubmit(event) {
    event.preventDefault();

    const form = event.target;
    const status = document.getElementById('form-status');
    const submitButton = form.querySelector('button[type="submit"]');

    // Get form data
    const name = form.name.value.trim();
    const message = form.message.value.trim();
    const website = form.website.value.trim();

    // Validate
    if (!name || !message) {
      this.showStatus('Please fill in all required fields.', 'error');
      return;
    }

    // Disable submit button
    submitButton.disabled = true;
    submitButton.textContent = 'Signing...';

    try {
      // Create entry object
      const entry = {
        name: name,
        message: message,
        website: website || null,
        approved: true // Auto-approve (you can change this to false for moderation)
      };

      // Save to Supabase
      const response = await fetch(
        `${this.supabaseUrl}/rest/v1/guestbook_entries`,
        {
          method: 'POST',
          headers: {
            'apikey': this.supabaseKey,
            'Authorization': `Bearer ${this.supabaseKey}`,
            'Content-Type': 'application/json',
            'Prefer': 'return=minimal'
          },
          body: JSON.stringify(entry)
        }
      );

      if (!response.ok) {
        throw new Error('Failed to save entry');
      }

      // Show success message
      this.showStatus('Thanks for signing! Your entry has been added!', 'success');

      // Reset form
      form.reset();
      document.getElementById('char-count').textContent = '0';

      // Reload entries after a moment
      setTimeout(() => this.init(), 2000);

    } catch (error) {
      console.error('Error submitting guestbook entry:', error);
      this.showStatus('Error submitting entry. Please try again.', 'error');
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = 'Sign Guestbook';
    }
  }

  // Show status message
  showStatus(message, type = 'info') {
    const status = document.getElementById('form-status');
    if (status) {
      status.textContent = message;
      status.className = `form-status ${type}`;
      status.style.display = 'block';

      setTimeout(() => {
        status.style.display = 'none';
      }, 5000);
    }
  }

  // Escape HTML to prevent XSS
  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

// Auto-initialize on page load
if (typeof window !== 'undefined') {
  window.Guestbook = Guestbook;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      if (document.getElementById('guestbook-container')) {
        const guestbook = new Guestbook();
        guestbook.init();
      }
    });
  } else {
    if (document.getElementById('guestbook-container')) {
      const guestbook = new Guestbook();
      guestbook.init();
    }
  }
}
