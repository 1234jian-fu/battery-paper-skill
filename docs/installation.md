# 安装与智能体适配

[返回 README](../README.md) · [使用入口](../SKILL.md) · [验证范围](validation.md)

Battery Paper Skill 是一个完整的 `SKILL.md` 技能目录。安装时保留 `references/`、`scripts/`、`agents/` 等配套文件；只复制 `SKILL.md` 会丢失写作指南和语料卡。目录名保持为 `battery-paper-skill`。

**选择一种安装方式即可。** 本项目已在维护者的 Codex 环境安装并检查文件一致性；下列其他平台的目录和命令依据官方文档核对，尚未逐个平台完成实际写作测试。文档核对日期：2026-10-30。

## 方式一：用 Skills CLI 选择智能体

[Vercel Labs Skills CLI](https://github.com/vercel-labs/skills) 支持从 GitHub 安装技能；当前版本要求 **Node.js 22.20 或更新版本**，并需要访问仓库。先查看可发现的技能，再安装：

```bash
npx skills add 1234jian-fu/battery-paper-skill --list
npx skills add 1234jian-fu/battery-paper-skill --skill battery-paper-skill
```

第二条命令会让你选择智能体和安装方式。默认安装到当前项目；加入 `-g` 后供当前用户的多个项目使用。也可只执行下面与你所用平台对应的一条：

```bash
# Codex
npx skills add 1234jian-fu/battery-paper-skill --skill battery-paper-skill -a codex -g

# Claude Code
npx skills add 1234jian-fu/battery-paper-skill --skill battery-paper-skill -a claude-code -g

# Cursor
npx skills add 1234jian-fu/battery-paper-skill --skill battery-paper-skill -a cursor -g

# Gemini CLI
npx skills add 1234jian-fu/battery-paper-skill --skill battery-paper-skill -a gemini-cli -g

# GitHub Copilot
npx skills add 1234jian-fu/battery-paper-skill --skill battery-paper-skill -a github-copilot -g

# OpenCode
npx skills add 1234jian-fu/battery-paper-skill --skill battery-paper-skill -a opencode -g
```

Windows 环境若无法建立符号链接，可在安装命令末尾加 `--copy`。PowerShell 若阻止执行 `npx.ps1`，可使用 `npx.cmd` 执行相同命令。安装后按后文的平台说明检查发现结果。

本仓库的技能入口就在根目录。Skills CLI 的发现逻辑会检查根目录的 `SKILL.md`，不需要另造 `skills/battery-paper-skill/` 子目录。以上兼容判断来自[官方 CLI 文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)、[平台代理表](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)及[发现逻辑](https://github.com/vercel-labs/skills/blob/main/src/skills.ts)，不代表本仓库已获平台认证。

## 方式二：按平台原生安装

下表列出默认目录。每个路径下都应有 `battery-paper-skill/SKILL.md`，不是把 `SKILL.md` 直接放在 `skills/` 下。`~` 表示用户主目录；Windows 通常对应 `%USERPROFILE%`。自定义配置目录的用户应采用宿主实际使用的位置。

| 平台 | 用户级目录 | 项目级目录 | 发现与调用 |
|---|---|---|---|
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `~/.agents/skills/` | `.agents/skills/` | CLI / IDE 用 `/skills` 或 `$battery-paper-skill`；桌面端在技能选择器选择 |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` | `.claude/skills/` | `/battery-paper-skill` |
| [Cursor](https://cursor.com/docs/skills) | `~/.cursor/skills/` | `.cursor/skills/` | Agent 聊天输入 `/`，搜索技能名 |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | `~/.gemini/skills/` | `.gemini/skills/` | `/skills list` 检查；在请求中指定使用技能 |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | `~/.copilot/skills/` | `.github/skills/` | `/skills list` 检查；`/battery-paper-skill` 调用 |
| [OpenCode](https://opencode.ai/docs/skills) | `~/.config/opencode/skills/` | `.opencode/skills/` | 请求使用 `battery-paper-skill`，智能体按需加载 |

部分平台也支持共享 `.agents/skills/` 目录；上表给出一套可直接采用的位置。Skills CLI 可以选用宿主支持的共享目录，因此它的安装位置不必与表中平台专用目录完全一致。

### Codex

在支持内置安装器的 Codex 对话中发送：

```text
使用 $skill-installer，从 https://github.com/1234jian-fu/battery-paper-skill
安装仓库根目录的 Skill，技能名称为 battery-paper-skill。
```

也可以用 Git 安装到当前官方文档推荐的用户级目录。

**Windows PowerShell：**

```powershell
$skillParent = Join-Path $env:USERPROFILE '.agents/skills'
git clone https://github.com/1234jian-fu/battery-paper-skill.git (Join-Path $skillParent 'battery-paper-skill')
```

**macOS / Linux：**

```bash
git clone https://github.com/1234jian-fu/battery-paper-skill.git "$HOME/.agents/skills/battery-paper-skill"
```

CLI / IDE 可通过 `/skills` 或 `$battery-paper-skill` 检查和调用；桌面端使用技能选择器，也可直接写“使用 battery-paper-skill”。官方文档说明会自动发现技能变化，未出现时重启 Codex。[Codex 官方说明](https://learn.chatgpt.com/docs/build-skills)

<details>
<summary>已有 <code>~/.codex/skills</code> 或自定义 <code>CODEX_HOME</code> 的安装</summary>

本项目维护环境的内置安装器使用 `$CODEX_HOME/skills`，默认是 `~/.codex/skills`。已有可正常识别的安装可继续使用实际路径，不必为了目录名称再装一份。下面是与这类安装器一致的 PowerShell 写法：

```powershell
$skillParent = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
git clone https://github.com/1234jian-fu/battery-paper-skill.git (Join-Path $skillParent 'battery-paper-skill')
```

此处描述的是已观察到的本地安装器行为；新安装的默认路径以前面的当前官方文档为准。若技能列表出现两个同名条目，检查是否在多个目录重复安装。

</details>

### Claude Code

把完整目录放入 `~/.claude/skills/battery-paper-skill/`；只对一个项目使用则放入项目的 `.claude/skills/battery-paper-skill/`。例如 macOS / Linux 的用户级安装：

```bash
git clone https://github.com/1234jian-fu/battery-paper-skill.git "$HOME/.claude/skills/battery-paper-skill"
```

在 Claude Code 中发送：

```text
/battery-paper-skill 请先阅读我的当前稿和图，检查这一段的证据顺序与表征措辞。
```

当前 Claude Code 会观察技能文件变化；若本次才创建顶层 `skills` 目录，运行 `/reload-skills`，旧版本可重新启动。这里介绍的是本地 Claude Code；本机个人目录不会自动提供给 Cowork 或云端会话。[Claude Code 官方说明](https://code.claude.com/docs/en/skills)

### Cursor

把完整目录放入 `~/.cursor/skills/battery-paper-skill/`，或项目的 `.cursor/skills/battery-paper-skill/`。例如 macOS / Linux：

```bash
git clone https://github.com/1234jian-fu/battery-paper-skill.git "$HOME/.cursor/skills/battery-paper-skill"
```

重新打开 Cursor 后，在 **Customize → Skills** 检查技能；在 Agent 聊天输入 `/` 并选择 `battery-paper-skill`。Cursor 也支持 `.agents/skills/` 与 `~/.agents/skills/`。

这里采用文件目录安装。本仓库当前没有 Cursor marketplace manifest，不能把“From GitHub Repository”的插件市场导入流程当成普通 Skill 的一键导入。个人技能用于 Cloud Agents 时另需平台的同步配置；自动化任务应采用项目技能。[Cursor 官方说明](https://cursor.com/docs/skills)

### Gemini CLI

Gemini CLI 自带技能安装命令，无需额外 Skills CLI：

```bash
# 当前用户可用
gemini skills install https://github.com/1234jian-fu/battery-paper-skill

# 或：只安装到当前论文项目
gemini skills install https://github.com/1234jian-fu/battery-paper-skill --scope workspace
```

在 Gemini 会话中运行下面两条，再发送实际写作请求：

```text
/skills reload
/skills list
```

```text
请使用 battery-paper-skill，先读取当前稿件和图，仅审查这段表征描述。
```

用户级与工作区分别采用 `.gemini/skills/`，也支持 `.agents/skills/` 别名。同名技能按发现层级决定优先级。[Gemini CLI 官方说明](https://geminicli.com/docs/cli/using-agent-skills/)

### GitHub Copilot

对于本地 Copilot CLI，可把完整目录放入 `~/.copilot/skills/battery-paper-skill/`。例如 macOS / Linux：

```bash
git clone https://github.com/1234jian-fu/battery-paper-skill.git "$HOME/.copilot/skills/battery-paper-skill"
```

在交互会话中检查并调用：

```text
/skills reload
/skills list
/battery-paper-skill 检查当前段落，保留数值、测试条件和结论强度。
```

需要与论文项目一起共享时，把整个技能目录复制到 `.github/skills/battery-paper-skill/`；复制时去掉技能自身的 `.git/`，让文件由论文项目的仓库管理。Copilot 的 IDE 与云端使用方式取决于具体产品和版本，本机个人目录不等于云端已安装。[技能目录说明](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)、[CLI 调用与重载](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)、[各使用界面说明](https://docs.github.com/en/copilot/concepts/customizations/agent-skills)

### OpenCode

把完整目录放入 `~/.config/opencode/skills/battery-paper-skill/`，或项目的 `.opencode/skills/battery-paper-skill/`。例如 macOS / Linux 的默认用户级安装：

```bash
git clone https://github.com/1234jian-fu/battery-paper-skill.git "$HOME/.config/opencode/skills/battery-paper-skill"
```

重新进入会话，发送：

```text
请加载 battery-paper-skill，先检查我的图和段落，再做句子—段落—文章三级审查。
```

OpenCode 通过内置 `skill` 工具按需加载技能，不能假定它自动生成与 Claude Code 相同的斜杠命令。配置为拒绝访问的技能不会显示。OpenCode 同时支持 `.claude/skills/` 和 `.agents/skills/` 兼容目录。[OpenCode 官方说明](https://opencode.ai/docs/skills)

## Windows 手动安装其他平台

不使用 Node.js 时，PowerShell 也可以直接 Git 克隆。只需把第一行的目录换成目标平台的用户级目录；下面以 Claude Code 为例：

```powershell
$skillParent = Join-Path $env:USERPROFILE '.claude/skills'
$skillTarget = Join-Path $skillParent 'battery-paper-skill'
git clone https://github.com/1234jian-fu/battery-paper-skill.git $skillTarget
Test-Path (Join-Path $skillTarget 'SKILL.md')
```

可替换为 `.cursor/skills`、`.gemini/skills`、`.copilot/skills` 或 `.config/opencode/skills`。最后返回 `True` 只说明入口文件存在，还需通过宿主的技能列表或实际加载确认发现成功。目标目录已存在时，先查看其版本和本地修改，不要再次克隆覆盖。

## 安装后的第一次使用

把稿件、图和必要的数据放在智能体可读取的项目目录，在对话中发送：

```text
使用 battery-paper-skill。
先读取我的当前稿、最新图和已有修改记录，保留已确认结构。
本次只处理：[图号 / 段落 / 小节 / 全文]。
目标期刊：[可选]。输出语言：[中文 / 英文 / 中英对照]。
每段写完先检查证据顺序和推理边界，再对照实际核读的同功能论文段落修改。
```

目录结构应至少包含：

```text
battery-paper-skill/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── review-protocol.md
│   ├── characterization-writing.md
│   ├── literature-corpus.md
│   └── corpus/
└── scripts/paper_workbench.py
```

辅助检查脚本使用 Python 标准库，已验证环境为 **Python 3.14.7**；其他版本尚未建立完整兼容性矩阵。安装和阅读技能本身无需运行这些脚本。文献检索、合法全文获取、PDF 阅读和 Word 编辑依赖智能体本身的工具，安装此 Skill 不会自动安装这些服务。论文 PDF 独立存放在空间充足的资料库，GitHub 仓库提供语料卡与来源定位。

## 更新与排查

**Skills CLI 安装：**

```bash
npx skills check
npx skills update battery-paper-skill
```

**Git 克隆安装：**在对应技能目录内先检查本地修改，再快进更新：

```bash
git status --short
git pull --ff-only
```

有本地修改时先保留自己的版本，再决定如何合并；手动复制或原生安装器安装的目录未必带 `.git/`，不能一律运行 `git pull`。更新后按各平台说明重新发现技能。

| 现象 | 检查位置 |
|---|---|
| 技能列表没有出现 | 目录层级、`SKILL.md` 大小写、宿主实际使用的配置目录，以及是否已重新加载 |
| 有技能名但缺少详细指南 | 是否只复制了入口文件；应保留整个仓库的技能配套目录 |
| 更新后仍使用旧规则 | 是否在用户级、项目级或共享目录装了多个同名版本；在新会话确认实际加载路径 |
| 可以加载但不能搜索或读 PDF | 宿主是否有相应工具和文件访问能力；这与技能安装是两个条件 |
| 本地能用，云端不能用 | 核对当前产品的云端技能来源，不能假定本机个人目录会自动上传 |

文档中的“支持”指宿主公开支持这种技能格式及安装位置，具体科研写作效果仍取决于模型、可见证据、工具和当前任务范围。

## 官方来源

以下页面于 2026-10-30 实际查阅；宿主后续版本若调整目录或命令，以对应官方文档为准。

| 项目 | 核对依据 |
|---|---|
| Codex | [Build skills](https://learn.chatgpt.com/docs/build-skills)：本地目录、安装器、发现与调用 |
| Claude Code | [Extend Claude with skills](https://code.claude.com/docs/en/skills)：目录、调用、热更新及云端差异 |
| Cursor | [Agent Skills](https://cursor.com/docs/skills)：发现目录、技能选择器、插件导入与同步 |
| Gemini CLI | [Managing Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/)：原生安装命令、安装范围与重载 |
| GitHub Copilot | [Adding skills for CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)、[CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)：目录、加载与命令 |
| OpenCode | [Agent Skills](https://opencode.ai/docs/skills)：本地目录、兼容目录与工具加载 |
| Vercel Skills CLI | [README](https://github.com/vercel-labs/skills)、[命令参考](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)、[平台目录](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)、[发现源码](https://github.com/vercel-labs/skills/blob/main/src/skills.ts)：Node.js 要求、参数和根目录入口 |
