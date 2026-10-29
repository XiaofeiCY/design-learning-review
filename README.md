# 设计学习与弹性评审

个人级、跨项目复用的设计评审与学习方法。先理解任务和已有能力，区分独立操作、依赖、分支及状态，再决定布局与视觉；按影响、不确定性和失败后果裁剪检查，用证据收敛取舍。

当前为可试用初版，尚未完成真实项目效果验证。

## 项目入口

- [当前状态](docs/status.md)：最新结论、验证范围及下一步。
- [维护与同步](docs/workflow.md)：维护源、个人安装副本与变更规则。
- [验证记录](docs/validation.md)：实际执行的合成对照与限制。
- [迁移记录](docs/migration.md)：来源、目录映射与归档边界。
- [历史交付](outputs/)：初版和优化版说明。

## 技能

| 目录 | 用途 |
|---|---|
| [skills/design-learning-review](skills/design-learning-review/SKILL.md) | 主入口：任务理解、弹性检查、能力选择、分歧收敛与学习 |
| [skills/impeccable-review](skills/impeccable-review/SKILL.md) | 从 Impeccable 改编的只读专业评审指导，不是官方完整工具链 |

## 安装与使用

将两个技能目录分别复制到个人 Codex 技能目录（通常为 `~/.codex/skills/`，如配置了 CODEX_HOME 则以其为准）。已有同名目录时先比较并备份，不直接覆盖未知修改。只复制 `skills/` 内两个目录，不复制整个仓库。可读取两个入口及参考资料即构成资料级安装，不运行第三方安装器或钩子。

调用示例：

```text
请用 $design-learning-review 只读评审当前设计方案。先阅读项目入口、当前状态和对应方案，按需读取 $impeccable-review。说明依据、实际使用能力、新增发现和待验证项，不直接开发或修改项目规则。
```

项目约束和用户授权优先。简单任务无需多工具、多代理或报告；读专业指导不等于独立审查。没有实际运行检测器或界面，就不能报告相应验证通过。

## 检查

运行仓库结构检查：

```text
python -X utf8 tests/validate_structure.py
```

检查覆盖命名、必要文件、引用、伴随能力和授权边界，不证明设计判断有效。行为验证与真实试用反馈见 docs/validation.md；必要时在具备 skill-creator 的环境额外运行其 quick_validate。

## 来源与许可

只读适配的上游版本、改编范围和 Apache-2.0 许可证在 [来源记录](skills/impeccable-review/references/source.md) 与 [许可证](skills/impeccable-review/LICENSE)。本项目未为其余自有内容声明新的开源许可证，不将上游许可泛化至整个仓库。
