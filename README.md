# Ten-Step Learning Skill

一个基于《软技能：代码之外的生存指南》“十步学习法”的 Codex / Agent Skill。

它不会只生成一份看起来完整的学习计划，而是把学习组织成两个阶段：

- 第 1～6 步只执行一次：了解全局、确定范围、定义目标、寻找资源、创建学习计划、筛选资源。
- 第 7～10 步对每个模块循环执行：浅尝辄止、动手操作、全面掌握、乐为人师。

## 能做什么

- 用户只给出一个学习主题时，也能主动建立可调整的学习方案并立即开始。
- 用可验收的作品或能力定义“学会”，避免把看完资料当成完成。
- 每个模块都包含最小知识、实践、针对性深入和教授复述。
- 使用“十步学习状态卡”跨对话保存进度。
- 对时效性强或高风险主题优先核验官方、原始或权威资料。

## 安装

克隆仓库：

```bash
git clone https://github.com/1247Const/ten-step-learning-skill.git
```

把 Skill 目录复制到 Codex 的个人 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R ten-step-learning-skill/skills/ten-step-learning ~/.codex/skills/
```

重新启动 Codex 或开启一个新任务，让 Skill 元数据重新加载。

## 调用示例

最小输入：

```text
用十步学习法带我学习 Kotlin 协程。
```

带约束的输入：

```text
我想系统学习力量训练计划设计。目前有基础解剖知识，每周能投入 4 小时，
希望 6 周后能为自己设计并解释一份训练计划。请按十步学习法带我学习。
```

跨对话继续：

```text
继续十步学习，这是我上次的状态卡：
[十步学习状态卡]
主题：……
当前模块：……
当前步骤：……
```

也可以控制节奏：

```text
只帮我完成前六步，我确认后再开始练习。
```

```text
检查我的第 10 步复述是否真正讲清楚了。
```

## 目录

```text
skills/ten-step-learning/
├── SKILL.md
├── evals/
│   └── evals.json
└── references/
    └── coaching-checklists.md
scripts/
└── validate_skill.py
```

## 校验

```bash
python3 scripts/validate_skill.py
```

测试集覆盖三种典型情况：信息完整的新主题、只有主题的宽泛输入，以及从第 8 步继续的学习会话。

## 方法来源与边界

十个步骤的名称与两阶段结构来自 John Sonmez 的《软技能：代码之外的生存指南》。本仓库是对方法的独立、操作化实现，不包含书籍正文，也不隶属于作者或出版社。

## License

[MIT](LICENSE)
