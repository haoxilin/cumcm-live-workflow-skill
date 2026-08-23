# cumcm-live-workflow-skill

**CUMCM（全国大学生数学建模竞赛）真题全流程实战技能手册** —— 一套经过真实竞赛检验、可执行的完整工作流：

**读题自查 → 建模出图 → LaTeX 论文 → 交叉审阅 → 填 result 模板 → AI 自查表终审 → 清理打包**

内置：题意理解红线、数值严谨性守则、自建基准与交叉验证方法、去 AIGC 特征清单（正文 4 维度 + 代码 6 特征）、韩中庚写作规范落地、LaTeX 编号与图表规范、2026 新版 AI 合规规定与 26 条自查表终审框架。

## 技能结构

```
cumcm-live-workflow/
└── SKILL.md                          # 主技能文件（触发条件 + 全流程 + 坑位清单 + 终审框架）
```

单个 Markdown 文件，轻量（<100KB），无第三方依赖，解压即用。

## 前置条件（使用本技能所需环境）

### 建模 / 代码环境
| 组件 | 要求 | 用途 |
|---|---|---|
| Python | 3.12+ | 建模与数据处理 |
| numpy / scipy / pandas | 最新稳定版 | 数值计算、求解、优化 |
| matplotlib | 最新稳定版 | 出图（300dpi，PNG+PDF 双格式） |
| openpyxl | 最新稳定版 | 填 result 模板 / 读附件 |
| scikit-learn、black（可选） | 最新稳定版 | 机器学习备选 / 附录代码格式化 |

> 国内 pip 建议使用清华镜像：`pip install X -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 论文排版环境（LaTeX）
| 组件 | 要求 | 用途 |
|---|---|---|
| LaTeX 发行版 | MiKTeX 或 TeX Live | xelatex 编译 |
| ctex 宏包 | 随发行版安装 | ctexart 文档类（中文排版） |
| 中文字体 | Windows 自带 SimSun / SimHei | 正文宋体、标题黑体 |
| pdftotext / pdftoppm（可选） | poppler 工具 | PDF 文本/页面提取，供审阅校验 |

### 网络
- 可访问 PyPI（装依赖）、GitHub（可选：对照参考解答/发布）

## 安装本技能所需环境

- **支持"技能（skills）"机制的 AI Agent 客户端**（主流 Agent 基本都支持，见下方安装方法）
- 磁盘空间：<1MB
- 无需管理员权限：解压复制即可，无需编译、无需装依赖

## 安装方法（通用）

本技能本质上是一份"喂给 Agent 的完整作战手册"，**任何能读取文件的 AI Agent 都可以使用**。三种方式任选：

### 方式 A：放入 Agent 的 skills 目录（推荐）
把解压后的 `cumcm-live-workflow/` 文件夹复制到你所用 Agent 的 skills 目录，重启或 `/reload-skills` 后即可被自动发现。常见 Agent 的目录位置：

| Agent | skills 目录（典型路径） |
|---|---|
| **Claude Code** | `~/.claude/skills/` 或项目内 `.claude/skills/` |
| **Cursor** | 项目内 `.cursor/skills/` |
| **Cline** | `~/.cline/skills/` |
| **Roo Code** | `~/.roo/skills/` |
| **Codex（OpenAI）** | `~/.codex/skills/` |
| **Windsurf** | 项目内 `.windsurf/skills/` 或对应 profiles 目录 |
| **Qwen Code / 通义灵码 等** | 查其 skills/plugins 文档，通常为 `~/.<agent>/skills/` |
| **Hermes** | 桌面版 `data\hermes-home\skills\software-development\`；命令行版 `~/.hermes/skills/` |

> 目录名/路径随版本会变，找不到时在你所用 Agent 的文档里搜 "skills directory" 即可。

### 方式 B：手工装载（不依赖 skills 机制）
会话开始时，直接让 Agent 读取 `SKILL.md` 全文（如"请先阅读 SKILL.md 并按其执行"）。任何 Agent 都适用，效果等同。

### 方式 C：发布到 Agent 的 skill hub（若支持）
如 Hermes 支持 `hermes skills publish cumcm-live-workflow`，其他 Agent 的 hub 机制同理，按各自文档操作。

## 使用触发

- 完整打一场数模竞赛（练手或正式比赛）
- 备赛训练、模拟完整流程
- 已出题、要求"按竞赛标准走完流程"
- 拿到成品论文，要求按 AI 自查表终审整改

## 版本记录

- **v1**：全流程实战（环境→读题→建模出图→论文→审阅→填表→打包）
- **v2**：基准对照修正（起点几何 / 矩形碰撞判据 / 解析速度传播）+ 教训固化
- **v3**：去 AIGC 特征（正文 4 维度 + 代码 6 特征）+ 无官方答案时题目自查 5 步
- **v4**：韩中庚写作指导落地（敏感性分析 / 假设讲理 / 模型评价四要素 / 标题排比）
- **v5**：LaTeX 编号与图表规范（引用必须 `\ref` 自动编号、双子图图题格式、附录编号体系、`\#` 转义、禁"与参考解答一致"表述）
- **v6**：编号体系规范（章节无括号数字 + 列表小括号，标题禁手写"问题X"前缀）
- **v7**：2026 AI 合规新规（AI 工具使用声明 + AI 详情 PDF）与 AI 自查表驱动终审——证据链核查法（参考校准 / 独立复算裁决 / xlsx 抽查 / 图表目检 / PDF 程序化测量）+ 敏感性实验实跑 + 编号体系 v7（列表罗马数字区分公式号 + align 用 `\notag` 合并单号）+ 终审整改联动检查
- **v7.1**：仓库化改造——README 通用化（多 Agent 安装方法 + 前置条件说明）
- **v7.2**：SKILL.md 全面去真题化（移除特定题目内容与本机环境信息），沉淀为通用实战手册；README 增加维护与更新说明

## 维护与更新

本仓库由 AI 智能体（Agent 会话）维护，更新流程如下：

1. 编辑 `cumcm-live-workflow/SKILL.md` 或 `README.md`
2. `git add -A && git commit`（提交说明写明版本号）
3. `git push`（需本机已 `gh auth login`；走代理时设置 `HTTPS_PROXY`）
4. 重新打包 `cumcm-live-workflow-skill-vX.Y.zip`（内容：README.md + cumcm-live-workflow/SKILL.md）
5. 发布新 Release 并附带 zip：`gh release create vX.Y <zip> --notes "更新摘要"`

> 对使用者的要求：仅本地 `git pull` 即可获取更新；zip 通过 Release 页面下载。
> 对维护者（Agent）的要求：gh 已授权登录（token 存于 `~/.config/gh/hosts.yml`）；推送走系统代理（如 `127.0.0.1:7897`）时需显式设置 `HTTPS_PROXY` 环境变量。

## 许可

MIT © 2026 haoxilin
