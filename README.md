# MEME6 实时指数

一个单文件静态网页，用于展示 MEME6 加权实时指数和成分币行情图表。

## 功能

- 实时获取 Binance Vision K 线数据
- 支持多周期切换
- K 线、成交量、MA、RSI 指标展示
- 支持拖拽查看历史、滚轮缩放、双击回到最新

## 本地预览

```bash
python3 -m http.server 8000
```

打开 <http://localhost:8000/>。

## 文件

- `index.html`：GitHub Pages 入口文件
- `meme-index.html`：原始页面文件
