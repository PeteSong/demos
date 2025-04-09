import asyncio

import demos.asyncio_demo as demo


def test_asyncio_demo(capsys):
    asyncio.run(demo.main())
    captured = capsys.readouterr()
    assert "hello" in captured.out
    assert "Task" in captured.out
    assert "Produced" in captured.out
    assert "Consumed" in captured.out
