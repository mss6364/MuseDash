# Frontend（前端入口）

交互流程（当前为占位逻辑，待接入后台）：
- 初始界面：全屏背景 + “点击任意位置开始游戏”。
- 点任意处后，底部出现“随机模式 / 普通模式”按钮。
- 普通模式：点击后调用 chart_analysis 解析 charts/ 下除 Random 外的全部谱面，并在 `chart_analysis/outputs/` 生成分析图与数据（建议 PNG + JSON）。前端会自动推导项目根路径，读取：
  - 图：`<根路径>/chart_analysis/outputs/<曲目名>_note_count.png`、`_note_density.png`、`_bpm_curve.png`
  - 数据：`<根路径>/chart_analysis/outputs/<曲目名>_summary.json`
  进入轮盘式选曲界面，悬停放大并预览分析图/音频（需后台支持），同时展示 summary JSON 里的数据摘要；点击选中后可触发写入 BPM & ROM、打开 Quartus。
- 随机模式：点击后调用 chart_engine 生成 Random 谱面，再调用 chart_analysis 生成分析图；完成后可开始（写入/启动）或重新生成。

文件说明：
- `index.html`：布局与样式（背景、起始提示、模式切换、普通/随机面板）。
- `app.js`：前端状态与事件，占位的后端调用（chart_engine、chart_analysis、Quartus 启动）。
- `assets/.gitkeep`：放置背景图（默认引用 `assets/bg.jpg`，可替换）。

对接后台时：
- 普通模式：提供获取曲目列表（排除 charts/Random）、音频预览地址、分析图 URL 的 API。
- 随机模式：提供“生成 Random 谱面 + 返回分析图”的 API。
- 写入流程：将选中曲目的 BPM/ROM 写入（chart_engine），并在需要时通过后端打开 `quartus/MuseDash.qsf`。

实现完成后更新该部分的详细实现思路doc（建议使用文件夹名.md的markdown文件）和相关的思路/流程图片，将用于最终报告和ppt
