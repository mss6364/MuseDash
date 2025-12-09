# Chart 引擎

目标：用 Python 替换旧 C++ 流程，生成 ROM.v 并更新顶层 BPM，支持随机/普通模式，可供前端/脚本调用。

实现要求（当前为占位，需按此补全）：
- 校验接口：`chart_check(chart_name) -> bool`
  - 输入曲目名，默认读取 `charts/<曲目名>/<曲目名>.txt`。
  - 校验：文件存在、基础格式、时间为整数且单调不减（同一时间可有不同轨道）、同一时间同一轨道不得重合（含长条与单点）。不通过返回 False。
- Verilog 生成接口：`process_chart(chart_name) -> bool`
  - 输入：曲目名（含 Random）。
  - 流程：读取 TXT -> 调用 `chart_check` -> 生成谱面模型 -> 生成 ROM 数据 -> 写入 `verilog/rom.v` -> 更新顶层 BPM（如需）。
  - 返回：布尔，表示是否成功完成生成与更新。
- 随机生成接口：`generate_random_chart`
  - 当前为空占位（不写入文件）。实现时应覆盖 `charts/Random/Random.txt`

目录说明：
- `chart_engine.py`：占位文件，仅保留 `chart_check` / `process_chart` / `generate_random_chart` / `main`，按上述要求补全。
- `outputs/`：ROM 生成输出目录。
- `legacy_cpp/`：原 C++ 流程（只读参考）。

实现完成后更新该部分的详细实现思路 doc（建议使用 markdown）和相关的思路/流程图片，用于最终报告和 ppt。
