# CF-multiple-account
`get_submission.py` 提供了获取 CF 提交记录的函数，`similarity.py` 提供了衡量两组代码码风相似度的函数。

你可以将 CF 上高 rating 选手的代码爬下来，随后与指定的一组代码依次比较码风的相似度，从而找到码风最像的一个用户。

你也可以求出码风对应的向量，再以向量的点积求出码风的相似度。如果你需要把一组代码多次用来比较，这样做可以提升效率。

不需要将 cookie 写入文件 `cookie` 中。

用法参见 `example.py`。
