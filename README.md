# INTO-CPS DTP

## Build instructions

If using `pipenv` the nessesary dependencies can be installed as follows:

```bash
pipenv install --dev
```
To build the tool use
```bash
pipenv run build
```
To release a new version do the following:
* `pipenv run build`
* `pipenv run twine_upload`
* login and allow the upload to complete
* increment version number for next release and commit it

Ask Casper for Permission / to deploy it.