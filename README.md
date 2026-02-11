# Reddit Demand Miner Skill Pack (需求挖掘技能包)

这套技能包旨在实现：**“支持挖取Reddit 3 个子领域 → 生成需求清单 → 挑选最值钱的方向做站”**。

## 包含的技能

1.  **Skill 1: Reddit Search (reddit_search)**
    *   **用途**：根据关键词、子版块和时间范围抓取 Reddit 帖子。
    *   **实现方式 (推荐)**：使用 Agent 内置的 `search_web` 工具进行 **Web Search Simulation** (模拟搜索 `site:reddit.com ...`)。这种方式不受 API 限制 (429/403)，且无需设置延时。

2.  **Skill 2: Intent/Pain Point Extract (reddit_extract)**
    *   **用途**：对抓取到的帖子进行 AI 结构化分析，提取痛点、需求类型和购买意图评分。
    *   **输入**：Skill 1 输出的帖子列表或搜索结果摘要。
    *   **AI 任务**：分析原句，标注求推荐/求替代/报错等类型。

3.  **Skill 3: Cluster & Output (reddit_cluster)**
    *   **用途**：将提取出的离散需求聚类，输出 10-30 个“可执行需求卡片”。
    *   **输出**：自动保存到 `find-need-skills/reddit_result/` 目录下，文件格式为 `result-YY-MM-DD.md`。
    *   **内容**：包含需求标题、目标用户、Reddit 证据句、页面大纲、SEO 关键词、变现建议。

## 推荐操作流程 (Workflow)

你可以直接命令 AI（OpenClaw / Antigravity / Claude Code）：

```
"请帮我挖掘 'Website Builder' 领域的最新需求。
1. 使用 `reddit_search` 的 Web Search Simulation 模式搜索 `webdev,saas,indiehackers` 版块过去一个月的帖子。
2. 将结果交给 `reddit_extract` 提取痛点和意图。
3. 最后用 `reddit_cluster` 生成 10 个可落地的做站选题卡片，并保存到 `find-need-skills/reddit_result/` 目录下（例如 `result-26-02-11.md`）。"
```

## 注意事项
- **抗封禁机制**：新版采用了 **Web Search Simulation** 模式，直接查询搜索引擎索引而非 Reddit 服务器。这意味着你 **不需要** 担心 IP 封禁或速率限制 (Rate Limits)，也 **不需要** 在请求间增加人工延时。
- **依赖**：仅在使用 Python 脚本（备用模式）时需要 Python 环境及 `requests` 库。
