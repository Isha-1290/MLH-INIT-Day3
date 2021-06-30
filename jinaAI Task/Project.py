from jina import Executor, Flow, requests


class MyExecutor(Executor):

    @requests
    def foo_need_pars_only(self, parameters, **kwargs):
        print(parameters)


f = Flow().add(uses=MyExecutor)

with f:
    f.post('/foo', parameters={'hello': 'world'})
