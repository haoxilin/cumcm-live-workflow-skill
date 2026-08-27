# cumcm-live-workflow-skill

**CUMCM（全国大学生数学建模竞赛）真题全流程实战技能手册** —— 一套经过真实竞赛检验、可执行的完整工作流：

**读题自查 → 建模出图 → LaTeX 论文 → 交叉审阅 → 填 result 模板 → AI 自查表终审 → 清理打包**

内置：题意理解红线、数值严谨性守则、自建基准与交叉验证方法、去 AIGC 特征清单（正文 4 维度 + 代码 6 特征）、论文写作规范落地、LaTeX 编号与图表规范、2026 新版 AI 合规规定与 26 条自查表终审框架。

## 技能结构

```
cumcm-live-workflow/
├── SKILL.md                          # 主技能文件（触发条件 + 全流程 + 坑位清单 + 终审框架）
└── references/                       # 可执行验证模板
    ├── verify_xlsx_rows.py           #   结果模板行映射与数值校验
    ├── verify_pdf_metrics.py         #   PDF 结构/越界/匿名/关键数字体检
    └── sensitivity_framework.py      #   敏感性实验跑批框架
templates/                            # 参考材料（直接下载使用）
├── 格式规范.pdf                      #   当届官方《论文格式规范》
├── AI工具使用规定(2026试行).pdf      #   2026 AI 合规红线
├── 2026数学建模国赛AI自查表.docx     #   26 条核查清单
├── 2026数学建模国赛标准论文Word模板.doc
└── 2026国赛国奖级论文AI自动优化升级提示词.docx   # 国奖级九模块升级标准与硬性指标核查清单
WORKED_EXAMPLE.md                     # 最小工作示例（水箱注水：从题面到可验证结果）
```

主技能文件为单个 Markdown，轻量（<100KB）；配套验证模板可直接改参数复用，参考材料直接下载使用。

## 使用前准备：喂给 AI 的初始材料

本技能是"作战手册"，开跑前请把以下**输入材料**备齐并放进项目目录（如 `2024A题/`），会话开始时把文件路径告诉 AI：

| 材料 | 必需性 | 用途 |
|---|---|---|
| **赛题原题**（PDF/doc） | ⭐ 必需 | 题目全文与全部数值约束，AI 题意分析与建模的唯一依据 |
| **当届《论文格式规范》** | ⭐ 必需 | 摘要页/页码/页数上限/附录要求，决定论文结构与排版 |
| **附件与结果模板**（如 result\*.xlsx） | 视题目 | 数据与输出模板；**只读**，填写后另存，不覆盖原附件 |
| **AI 工具使用规定**（2026 试行） | ⭐ 必需 | AI 使用声明、AI 详情 PDF 等合规硬性要求 |
| 参赛通知 / 竞赛规则 | 建议 | 提交时间、文件格式、支撑材料要求 |
| 获奖范文 / 参考解答 | 可选 | 答案数值校准与写作风格参考（模拟训练时） |
| 写作方法指导 | 可选 | 论文结构规范参考 |

**推荐的开场指令（示例）**：

> 按 cumcm-live-workflow 技能执行。材料在 `<题号>/` 目录：原题、格式规范、附件（如有）。请从读题自查开始，走完全流程。

AI 会依次执行：**读题自查 → 建模出图 → LaTeX 论文 → 交叉审阅 → 填 result 模板 → AI 自查表终审 → 清理打包**。

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

**启动关键词**（对 Agent 说出任一即启动本技能）：
- 流程类："完整做真题""按竞赛标准走完流程""数学建模竞赛实战""打国赛""备赛训练"
- 环境类："环境检查""检查环境""准备环境""环境就绪"
- 终审类："按 AI 自查表审查""自查表终审""论文终审整改"

**启动后行为**：技能自动执行环境检查（Python/依赖库/LaTeX/ctex 等），输出**前置条件完成度清单**；经你确认后自动安装缺失组件（pip 走清华镜像，LaTeX 用 winget），装完复测到就绪再进入读题环节。

具体场景：
- 完整打一场数模竞赛（练手或正式比赛）
- 备赛训练、模拟完整流程
- 已出题、要求"按竞赛标准走完流程"
- 拿到成品论文，要求按 AI 自查表终审整改

## 版本记录

- **v5.0（2026-08-25 一次发布）**：
  - 启动关键词（流程/环境/终审三类）与启用后自动环境检测、确认后自动安装
  - 顶刊级图表规范（中文标签/统一配色）、五段式摘要、文献与公式扩充标准、降重四层法与九类 AI 痕迹自查、国奖级硬性指标清单
  - 论文成品结构模板（完整章节目录，每问固定三小节，编号统一）
  - 配套可执行验证模板（references/：xlsx 校验/PDF 体检/敏感性跑批）、最小工作示例（WORKED_EXAMPLE.md）、参考材料（templates/：格式规范/AI规定/自查表/Word模板/国奖级提示词）
  - 历史迭代（v1-v4 及内部过程）已归档于 CHANGELOG.md，主页不再展示中间版本

完整的变更历史见 [CHANGELOG.md](./CHANGELOG.md)。

## 维护与更新

本仓库由 AI 智能体（Agent 会话）维护，更新流程：

1. 编辑 `cumcm-live-workflow/SKILL.md` 或 `README.md`
2. `git add -A && git commit`（提交说明写明版本号）
3. `git push origin main`（本地仓库已配置认证与代理，无需额外操作）
4. 有新版本时：重打包 `cumcm-live-workflow-skill-vX.Y.zip`（内容：README.md + cumcm-live-workflow/SKILL.md），创建新 Release 并上传 zip 附件

**本地推送认证说明**（维护者须知）：仓库级 `.git/config` 已配置 `http.extraheader`（`Authorization: Basic <base64(用户名:token)>`，基于 GitHub Personal Access Token）与 `http.sslbackend=openssl`；推送前设置代理环境变量（本机 `HTTPS_PROXY=http://127.0.0.1:7897`）。GitHub 的 git 端点只接受 Basic 认证（Bearer/token 方案会 401），且 extraheader 是**多值配置**，重复设置会导致 "Duplicate header: Authorization" 400 错误——设置前先 `git config --unset-all http.extraheader`。

> 对使用者的要求：`git clone` 或 `git pull` 即可获取更新；zip 通过 Releases 页面下载。
> 安全提示：若 PAT 需轮换，请到 GitHub Settings → Developer settings → Personal access tokens 撤销旧 token，并在本地重跑 `git config http.extraheader "Authorization: Basic <base64(用户名:新token)>"`。

## 许可

MIT © 2026 haoxilin
