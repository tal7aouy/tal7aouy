from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("🤓 [link=https://www.talhaouy.me]Med Talhaouy", guide_style="bold cyan")
python_tree = tree.add("🐘 PHP|Laravel Expert", guide_style="green")
python_tree.add("✅ Node.js")
python_tree.add("✅ Python")
python_tree.add("✅ JavaScript")
python_tree.add("✅ TypeScript")
full_stack_tree = tree.add("🔧 Решение проблем")

about = """ Я инженер-программист, может быть, не очень серьезно отношусь к себе, но очень серьезно отношусь к своей работе и люблю 
решать проблемы, а не жаловаться на них.

[green]Следите за мной в twitter [bold link=https://twitter.com/tal7aouy]@tal7aouy[/]"""

panel = Panel.fit(
  about, box=box.DOUBLE, border_style="blue", title="[b]Здравствуйте", width=60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
