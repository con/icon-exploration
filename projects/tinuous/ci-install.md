# tinuous PR 234 installation CI diagnosis

PR: https://github.com/con/tinuous/pull/234
Failed workflow run: https://github.com/con/tinuous/actions/runs/38331385635
Head: `95754c5c391245feb961cd3abe521630a1420d39`

## Diagnosis

Both `test (base)` (job `115081664918`) and `test (datalad)` (job
`115081665104`) completed the package installation step. They failed later in
`coverage run --source tinuous --branch -m tinuous fetch` when the integration
test tried to authenticate to CircleCI. The failure was:

> RuntimeError: CircleCI token not set. Set via CIRCLECI_CLI_TOKEN environment
> variable or log in with `circleci` client.

PR 234 is cross-repository (`leej3/tinuous` to `con/tinuous`), so GitHub does
not expose repository secrets to these jobs. Both jobs therefore have the same
secret-availability failure. The submitted logo/icon changes do not touch
installation code or workflow configuration, so they did not cause this
failure.

The workflow now keeps installation active for fork PRs and skips only the
secret-dependent fetch and its coverage report/upload. Those steps still run on
pushes and same-repository PRs.

## Validation

- Duct run `20261013T012517.651237Z-d83591269d5244199ba7ebedb113fe3a`:
  isolated `pip install .` plus `tinuous --help` passed (exit 0).
- Parsed `.github/workflows/inception-test.yml` with PyYAML and confirmed the
  fork-PR condition is present on all three integration/coverage steps.
- `git diff --check` passed.
- Original job logs are retained as `job-115081664918-base.log` and
  `job-115081665104-datalad.log` in this directory.

An unrelated pending external check is AppVeyor:
https://ci.appveyor.com/project/yarikoptic/tinuous/builds/54884584
