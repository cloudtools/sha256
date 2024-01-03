Steps to release a new version
------------------------------

- Install the build tools: `python3 -m pip install --upgrade build twine`
- Change version in setup.py and sha256.pyx
- Create a signed tag: ``git tag --sign -m "Release 1.1.1" 1.1.1``
- Build the distribution: python3 -m build
- Use twine to check the release: twine check dist/sha256-1.1.1*.gz
- Upload using twine: twine upload -s dist/sha256-1.1.1*.gz
- Push commits: ``git push``
- Push tag: ``git push --tags``
- Update github release page: https://github.com/cloudtools/sha256/releases
