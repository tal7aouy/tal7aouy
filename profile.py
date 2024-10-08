from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=110)

tree = Tree("🤓 [link=https://www.talhaouy.me]Mhamed Talhaouy", guide_style="bold cyan")
python_tree = tree.add("🐘 PHP|Laravel Expert", guide_style="green")
python_tree.add("➫ Nodejs | Vuejs")
python_tree.add("➫ LangChain | PyTorch | Pandas | Numpy")
python_tree.add("➫ PHP | Python | Js | Solidity")
python_tree.add("➫ AWS | CI/CD | Nginx")
python_tree.add("➫ MySQL | Docker | Redis")
full_stack_tree = tree.add("🧹 Clean Coder")

about = """
I'm a software engineer with a passion for building things, breaking things, and building things that break things, but not breaking things that build things - that's just mean.
[green]Follow me on twitter [bold link=https://twitter.com/tal7aouy]@tal7aouy[/]"""


panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]👋 Hey there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
