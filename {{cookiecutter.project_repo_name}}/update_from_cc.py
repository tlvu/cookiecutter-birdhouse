from cookiecutter.main import cookiecutter

if __name__ == "__main__":

    cookiecutter('cookiecutter-birdhouse',
                 no_input=True,
                 overwrite_if_exists=True,
                 extra_context={
                   "full_name": "{{ full_name }}",
                   "email": "{{ email }}",
                   "github_username": "{{ github_username }}",
                   "project_name": "{{ project_name }}",
                   "project_slug": "{{ project_slug }}",
                   "project_repo_name": " {{ project_repo_name }}",
                   "project_short_description": "{{ project_short_description }}",
                   "version": "{{ version }}",
                   "open_source_license": "{{ open_source_license ",
                   "http_port": "{{ http_port }}",
                   "_timestamp": "{{ _timestamp }}"
                 }
                 )
