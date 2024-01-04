import nox


nox.options.error_on_external_run = True
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["tests-3"]


@nox.session(python='3')
def tests(session):
    session.install('-e', '.')
    session.run('python3', '-m', 'unittest', *session.posargs)
