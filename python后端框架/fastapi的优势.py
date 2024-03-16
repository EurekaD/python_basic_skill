"""
FastAPI 的构建考虑了以下三个主要问题：

速度
开发者经验
开放标准

你可以把 FastAPI 看作是把 Starlette、Pydantic、OpenAPI 和 JSON Schema 粘合在一起的胶水。

本质上说，FastAPI 使用 Pydantic 进行数据验证，并使用 Starlette 作为工具，使其与 Flask 相比快得惊人，具有与 Node 或 Go 中的高速 Web APIs 相同的性能。
Starlette + Uvicorn 提供异步请求能力，这是 Flask 所缺乏的。
有了 Pydantic 以及类型提示，你就可以得到一个具有自动完成功能的良好的编辑体验。你还可以得到数据验证、序列化和反序列化（用于构建一个 API），以及自动化文档（通过 JSON Schema 和 OpenAPI ）。
也就是说，Flask 的使用更为广泛，所以它经过了实战检验，并且有更大的社区支持它。由于这两个框架都是用来扩展的，Flask 显然是赢家，因为它有庞大的插件生态系统。

建议：
如果你对上述三个问题有共鸣，厌倦了 Flask 扩展时的大量选择，希望利用异步请求，或者只是想建立一个 RESTful API，请使用 FastAPI。
如果你对 FastAPI 的成熟度不满意，需要用服务器端模板构建一个全栈应用，或者离不开一些社区维护的 Flask 扩展，就可以使用 Flask。

"""