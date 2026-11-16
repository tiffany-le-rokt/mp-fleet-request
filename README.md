# mp-fleet-request

A Claude skill that turns mParticle platform feature requests and bugs (SDKs, integrations, identity, audiences) into Fleet-ready requirements. It interviews the requester like a PM mentor, shows a preview, then posts the request to an mParticle Fleet Google Chat room or saves it as a Google Doc or .md file.

## Contents

| Path | What it is |
|---|---|
| `mp-fleet-request/SKILL.md` | The skill. This single file is everything Claude needs. Upload it as a skill in Claude. |
| `mp-fleet-request/template/mP Fleet Request Template.docx` | Backup export of the Rokt internal template. |
| `mp-fleet-request/template/format_requests.py` | Standalone copy of the formatting script that is embedded in SKILL.md. |

## How the Google Doc output works

When a skill is saved in Claude, only SKILL.md is kept, so the skill does not read the template from this repo. It copies the live Google Doc template and fills in the copy:

- **mP Fleet Request Template** (Google Doc): https://docs.google.com/document/d/1wWbXdRC31kczVFd-bqW4EbatR0iIe3MEWgDYTvKf0fM/edit
- File ID `1wWbXdRC31kczVFd-bqW4EbatR0iIe3MEWgDYTvKf0fM` is set in SKILL.md.
- Everyone who uses the skill needs view access to that Google Doc.

To change the template, edit the Google Doc directly and keep the `{{PLACEHOLDER}}` tokens. If you replace the Google Doc with a new one, upload the .docx in `template/` to Drive as a Google Doc and update the file ID in SKILL.md.

## Updating the skill

1. Edit `mp-fleet-request/SKILL.md` here.
2. Upload the new SKILL.md to Claude, replacing the existing mp-fleet-request skill.
