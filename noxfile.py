"""Nox sessions."""
from pathlib import Path
import shutil

import nox
from nox.sessions import Session

@nox.session
def docs(session: Session) -> None:
    """Build the documentation."""
    session.install("-r", "docs/requirements.txt")

    if session.interactive:
        session.run("mkdocs", "serve")
    else:
        session.run("mkdocs", "build")