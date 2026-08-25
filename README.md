# cumcm-live-workflow-skill

**CUMCM（全国大学生数学建模竞赛）真题全流程实战技能手册** —— 一套经过真实竞赛检验、可执行的完整工作流：

**读题自查 → 建模出图 → LaTeX 论文 → 交叉审阅 → 填 result 模板 → AI 自查表终审 → 清理打包**

内置：题意理解红线、数值严谨性守则、自建基准与交叉验证方法、去 AIGC 特征清单（正文 4 维度 + 代码 6 特征）、论文写作规范落地、LaTeX 编号与图表规范、2026 新版 AI 合规规定与 26 条自查表终审框架。

## 技能结构

```
cumcm-live-workflow/
└── SKILL.md                          # 主技能文件（触发条件 + 全流程 + 坑位清单 + 终审框架）
```

单个 Markdown 文件，轻量（<100KB），无第三方依赖，解压即用。

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

- 完整打一场数模竞赛（练手或正式比赛）
- 备赛训练、模拟完整流程
- 已出题、要求"按竞赛标准走完流程"
- 拿到成品论文，要求按 AI 自查表终审整改

## 版本记录

- **v5 · 国奖级指标与图表中文化（当前）**：顶刊级图表规范（中文标签/统一配色/正交流程图/箭头止于框边）、五段式摘要、文献与公式扩充标准、降重四层法与九类 AI 痕迹自查、国奖级硬性指标清单
- **v4 · 开源仓库化**：通用化改造——多 Agent 安装方法、前置条件说明、喂给 AI 的初始材料清单；内容去真题化与表述中性化
- **v3 · AI 合规与终审**：2026 AI 合规新规（AI 工具使用声明 + AI 详情 PDF）；AI 自查表驱动终审与证据链核查法（参考校准 / 独立复算 / 数据抽查 / 图表目检）；敏感性实验实跑；编号体系优化
- **v2 · 质量与规范**：去 AIGC 特征清单（正文 4 维度 + 代码 6 特征）；写作规范落地（敏感性分析 / 假设讲理 / 模型评价四要素）；LaTeX 编号与图表规范
- **v1 · 全流程框架**：读题自查 → 建模出图 → LaTeX 论文 → 交叉审阅 → 填 result 模板 → 打包交付的完整工作流；题意理解红线与数值严谨性守则

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
