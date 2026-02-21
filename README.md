# Django Blog Management System

A full-featured blog platform built with Django that supports multi-user authentication with role-based access control. The system includes a powerful dashboard for managers and editors to create, manage, and publish blog posts.

## Features

### User Features

- 🔐 User registration and authentication
- 📝 Read and browse blog posts
- 💬 Comment on blog posts (authenticated users only)
- 🏷️ Browse posts by category
- 🔍 Search functionality

### Dashboard Features (Manager & Editor)

- 📊 Dedicated dashboard for content management
- ✍️ Create, edit, and delete blog posts
- 📂 Category management
- 🖼️ Featured image uploads
- 👥 Role-based access control
- 📈 Content overview and statistics

### Technical Features

- Responsive design using Bootstrap
- Clean and intuitive UI/UX
- SEO-friendly URLs
- Image upload and management
- WYSIWYG editor support (optional)
- Secure authentication system

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQLite (default) / PostgreSQL / MySQL
- **Authentication:** Django's built-in authentication system
- **Package Management:** uv (fast Python package installer)

## Installation

### Prerequisites

- Python 3.8 or higher
- uv (Fast Python package installer and resolver)

### Setup Instructions

1. **Install uv** (if not already installed)

   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # Or using pip
   pip install uv
   ```

2. **Clone the repository**

   ```bash
   git clone https://github.com/mayank698/Django-blog.git
   cd django-blog
   ```

3. **Create and activate virtual environment with uv**

   ```bash
   # Create virtual environment
   uv venv

   # Activate virtual environment
   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   uv pip install -r requirements.txt

   # Or sync dependencies (if using pyproject.toml)
   uv pip sync requirements.txt
   ```

5. **Configure environment variables**
   Create a `.env` file in the project root:

   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

6. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

8. **Collect static files** (for production)

   ```bash
   python manage.py collectstatic
   ```

9. **Run the development server**

   ```bash
   python manage.py runserver
   ```

10. **Access the application**
    - Website: `http://127.0.0.1:8000/`
    - Admin Panel: `http://127.0.0.1:8000/admin/`
    - Dashboard: `http://127.0.0.1:8000/dashboard/`

## User Roles

### Manager

- Full access to all dashboard features
- Can create, edit, and delete all blog posts
- Can manage categories
- Can manage users and permissions

### Editor

- Can create and edit their own blog posts
- Can manage categories
- Limited access to user management

### Regular User

- Can register and login
- Can read blog posts
- Can comment on posts
- Cannot access dashboard

## Project Structure

```
django-blog/
├── blog/                   # Main blog app
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py          # Blog, Category, Comment models
│   ├── views.py           # View functions
│   ├── urls.py            # URL routing
│   └── forms.py           # Forms
├── dashboard/             # Dashboard app
│   ├── migrations/
│   ├── templates/
│   ├── views.py           # Dashboard views
│   └── urls.py
├── accounts/              # User authentication app
│   ├── views.py           # Login, register, logout
│   └── urls.py
├── media/                 # Uploaded files
├── static/                # Static files (CSS, JS, images)
├── templates/             # Base templates
├── manage.py
├── requirements.txt
└── README.md
```

## Usage

### For Users

1. Register for an account or login
2. Browse blog posts on the homepage
3. Click on a post to read the full article
4. Leave comments (requires login)
5. Filter posts by category

### For Managers/Editors

1. Login with manager or editor credentials
2. Access the dashboard at `/dashboard/`
3. Create new blog posts with the "Add New" button
4. Manage categories from the Categories section
5. Edit or delete existing posts
6. View all comments and moderate if needed

### Media Files

Ensure media files are properly configured in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

## Security Considerations

- Keep `SECRET_KEY` confidential
- Set `DEBUG = False` in production
- Use environment variables for sensitive data
- Implement HTTPS in production
- Regular security updates for dependencies
- Use strong passwords for admin accounts

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## Acknowledgments

- Django documentation
- Bootstrap for UI components
- Font Awesome for icons
- Django community for helpful resources

## Support

For issues, questions, or suggestions:

- Open an issue on GitHub
- Contact: your-email@example.com

## Roadmap

- [ ] Add rich text editor (CKEditor/TinyMCE)
- [ ] Implement post scheduling
- [ ] Add social media sharing
- [ ] Email notifications for comments
- [ ] Advanced search with filters
- [ ] Post analytics and views tracking
- [ ] Multi-language support
- [ ] API endpoints (Django REST Framework)

---

**Made with ❤️ using Django**
