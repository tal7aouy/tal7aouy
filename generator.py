from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 [link=https://www.talhaouy.me]Med Talhaouy", guide_style="bold cyan")
python_tree = tree.add("🐘 PHP|Laravel Expert", guide_style="green")
python_tree.add("⭐ Node.js")
python_tree.add("⭐ Symfony")
python_tree.add("⭐ Vue.js")
python_tree.add("⭐ Docker")
python_tree.add("⭐ Redis")
full_stack_tree = tree.add("🔧 Problem Solver")

about = """\
I'm a software Engineer, living in [link=]Casablanca[/], Morocco. I may not take myself very seriously but take my job very seriously and loves solving problems instead of complaining about them.

[green]Follow me on twitter [bold link=https://twitter.com/tal7aouy]@tal7aouy[/]"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hi there", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
