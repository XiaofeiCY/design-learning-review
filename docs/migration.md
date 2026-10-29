# 立项与迁移记录

日期：2026-10-29。用户授权迁移至 `E:\work\design-learning-review` 并推送指定 GitHub 仓库。迁移前目标目录为空，远端无分支提交，默认分支 master。

## 映射

| 来源内容 | 新位置 | Git |
|---|---|---|
| 个人已安装的两个 Skill | skills/design-learning-review 与 skills/impeccable-review | 纳入，作为维护源 |
| 历史交付说明 | outputs/ | 纳入 |
| 旧状态快照 | archive/original-chat/docs/ | 仅本地归档 |
| 原工作目录、旧版备份、上游隔离资料 | archive/original-chat/work/ | 仅本地归档 |
| 合成评审输入 | tests/fixtures/review-fixture.md | 纳入 |
| 新项目入口及维护记录 | README.md、docs/ | 纳入 |

旧聊天目录暂留完整安全副本和迁移指引，不再作为维护源；未作删除操作。个人技能副本保留调用，新仓库不影响其他业务项目。下载资料、重复副本与本地归档由 .gitignore 排除，不作为第三方完整官方流程发布。

## 迁移验收

按相对路径及 SHA-256 校验两个 Skill、历史交付及原始 docs/work 归档；运行结构检查与官方 Skill 格式验证；提交前核对暂存文件、排除资料和提交内容；推送后确认 HEAD 与远端 master 一致并确认工作区干净。

实际完成结果将在迁移后追加。

本地验收完成：160 个来源文件逐项 SHA-256 一致；两个 Skill 通过官方 quick_validate；仓库结构检查通过；archive/ 已确认被 Git 忽略。旧目录为保留的安全副本，不是维护源。

远端验收完成：初始提交 c9853ce 已推送至 origin/master，核对本地 HEAD 与远端分支一致。归档保留本地，22 个维护文件已入库。
