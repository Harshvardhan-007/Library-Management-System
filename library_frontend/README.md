# LibraryHub - HTML/CSS/JavaScript Version

This is a complete library management system built with vanilla HTML, CSS (Tailwind CSS via CDN), and JavaScript.

## 📁 File Structure

```
public/
├── index.html          - Landing page (homepage)
├── login.html          - Login page
├── signup.html         - Signup page (to be created)
├── dashboard.html      - Student dashboard
├── search.html         - Search results page (to be created)
├── book-detail.html    - Book detail page (to be created)
├── account.html        - Student account page (to be created)
├── admin.html          - Admin dashboard (to be created)
├── admin-books.html    - Admin book management (to be created)
├── admin-overdues.html - Admin overdues management (to be created)
├── styles.css          - Custom CSS styles
├── app.js              - Shared JavaScript functionality
└── README.md           - This file
```

## 🚀 Getting Started

### Option 1: Open Directly in Browser
Simply open `index.html` in your web browser. All pages are standalone and don't require a server.

### Option 2: Use a Local Server (Recommended)
For better development experience:

**Using Python:**
```bash
cd public
python -m http.server 8000
```
Then visit: http://localhost:8000

**Using Node.js (http-server):**
```bash
npm install -g http-server
cd public
http-server -p 8000
```
Then visit: http://localhost:8000

**Using VS Code Live Server:**
1. Install "Live Server" extension
2. Right-click on `index.html`
3. Select "Open with Live Server"

## 🔑 Demo Credentials

### Admin Login:
- Email: `admin@lib.com`
- Password: `admin123`
- Redirects to: Admin Dashboard

### Student Login:
- Email: Any email (e.g., `student@example.com`)
- Password: Any password
- Redirects to: Student Dashboard

## 📱 Pages Overview

### Public Pages
- **index.html** - Landing page with hero section, features, and recently added books
- **login.html** - Login form with demo credentials
- **signup.html** - Registration form (to be created)

### Student Pages (Requires Login)
- **dashboard.html** - Personalized dashboard with borrowed books, fines, search, and recommendations
- **search.html** - Search results with filters and grid/list view (to be created)
- **book-detail.html** - Detailed book information with borrow/reserve options (to be created)
- **account.html** - Account management with tabs for borrowed books, fines, history, wishlist, and QR card (to be created)

### Admin Pages (Requires Admin Login)
- **admin.html** - Admin dashboard with metrics and quick actions (to be created)
- **admin-books.html** - Book inventory management with CRUD operations (to be created)
- **admin-overdues.html** - Overdue books management with bulk actions (to be created)

## 🎨 Design System

### Colors
- Primary: `#2C5F7C` (Blue Trust)
- Secondary: `#4A9B7F` (Green Success)
- Destructive: `#FF6B6B` (Coral Alert)
- Background: `#F8F9FA`
- Foreground: `#2D3748`

### Typography
- Font: Inter (via system fonts)
- Base size: 16px
- Line height: 1.6

### Spacing
- Grid: 4px base (p-1=4px, p-2=8px, p-3=12px, p-4=16px, etc.)

### Components
- Buttons: h-12 (48px), px-6 (24px), rounded-xl (12px)
- Cards: rounded-2xl (16px), shadow-md/lg/xl
- Status Badges: px-3 py-1, rounded-full, text-xs

## 🌙 Features

### Dark Mode
- Toggle button in header
- Persists in localStorage
- Supports system preference

### Authentication
- Demo login system using localStorage
- Role-based routing (student/admin)
- Protected pages with auth check

### Responsive Design
- Mobile-first approach
- Breakpoints: 375px (mobile) → 1440px (desktop)
- Touch-friendly (44px min touch targets)

### Accessibility
- ARIA labels
- Keyboard navigation
- 4.5:1 color contrast ratio
- Semantic HTML

## 🛠️ JavaScript Functions

### Theme Management
- `toggleDarkMode()` - Toggle dark/light theme
- `initDarkMode()` - Initialize theme from localStorage

### Authentication
- `Auth.login(email, password)` - Login user
- `Auth.logout()` - Logout user
- `Auth.getUser()` - Get current user
- `Auth.isAuthenticated()` - Check if user is logged in
- `requireAuth()` - Protect pages (redirect if not logged in)

### UI Utilities
- `showToast(message, type)` - Show toast notification
- `toggleDropdown(id)` - Toggle dropdown menu
- `toggleSidebar()` - Toggle mobile sidebar
- `openModal(modalId)` / `closeModal(modalId)` - Modal management
- `switchTab(tabName, groupName)` - Tab switching
- `togglePassword(inputId)` - Show/hide password
- `setViewMode(mode)` - Toggle grid/list view

### Form Utilities
- `validateEmail(email)` - Email validation
- `validateForm(formId)` - Form validation

### Storage
- `Storage.set(key, value)` - Save to localStorage
- `Storage.get(key)` - Get from localStorage
- `Storage.remove(key)` - Remove from localStorage

## 📝 Creating New Pages

To create additional pages, follow this template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title - LibraryHub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="styles.css">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        primary: '#2C5F7C',
                        secondary: '#4A9B7F',
                        destructive: '#FF6B6B',
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-gray-50 dark:bg-gray-900">
    <!-- Your content here -->
    
    <script src="app.js"></script>
    <script>
        // Page-specific JavaScript
        initDarkMode();
    </script>
</body>
</html>
```

## 🔄 Navigation Flow

```
index.html (Landing)
  ├── login.html
  │   ├── dashboard.html (Student) → search.html → book-detail.html
  │   │                            → account.html
  │   └── admin.html (Admin) → admin-books.html
  │                          → admin-overdues.html
  │                          → admin-users.html (to be created)
  │                          → admin-reports.html (to be created)
  └── signup.html → login.html
```

## ✅ All Pages Complete

All pages have been successfully created:

1. ✅ **index.html** - Landing page
2. ✅ **login.html** - Login page
3. ✅ **signup.html** - Registration form
4. ✅ **dashboard.html** - Student dashboard
5. ✅ **search.html** - Search results with filters
6. ✅ **book-detail.html** - Detailed book view
7. ✅ **account.html** - Student account with tabs
8. ✅ **admin.html** - Admin dashboard
9. ✅ **admin-books.html** - Book CRUD management
10. ✅ **admin-overdues.html** - Overdue management

## 📦 Dependencies

- **Tailwind CSS** - Loaded via CDN (no build process needed)
- **No other dependencies** - Pure vanilla JavaScript

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## 📄 License

This project is for educational purposes.

---

**Need Help?**
All functionality is documented in `app.js`. Check the comments for detailed explanations.
