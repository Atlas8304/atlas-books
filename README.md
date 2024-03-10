# Atlas Books - (Python / Django Coding Assignment)
A small website that allows users to look at a selection of books on library, logged in users can benefit from adding books to a personal list.


### Pre-Setup Requirements
Ubuntu or Windows set up with WSL is required currently for this project. It is untested in other environments and not guaranteed to function correctly.
1. Clone Repo to your designed location
1. Inside the newly created repo, at the projects base directory establish a new virtual environment
	1. `python -m venv env` using `.env` should conform to current `gitignore` rules
1. Inside the virtual environment
	1. Install `pip-tools` using `pip install pip-tools`
	1. Navigate to the `setup` folder
	1. Run `pip-sync` to install all necessary packages for development

### Quick Setup
1. Copy `.env.sample` to `.env`
1. Run `docker-compose up --build`
1. Create superuser `docker-compose exec web python manage.py createsuperuser`
1. Navigate to `http://localhost:8000/` in your browser

### Unit Tests
1. Connect to the `web` container via Shell
1. Ensure you are in the `/app` folder
1. Run `python manage.py test` 