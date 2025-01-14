from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

# Initialize Console
console = Console(record=True, width=120)

# Expertise Tree
tree = Tree("🤓 [link=https://talhaouy.me]Mhammed Talhaouy", guide_style="bold cyan")
expertise_tree = tree.add("💻 Senior Software Engineer | Web3 & Security Enthusiast", guide_style="bold green")
expertise_tree.add("🐘 PHP | Laravel Specialist")
expertise_tree.add("🚀 Node.js | Vue.js")
expertise_tree.add("🧠 LangChain | PyTorch | Pandas | NumPy")
expertise_tree.add("🛠️ Solidity | Smart Contracts")
expertise_tree.add("☁️ AWS | CI/CD Pipelines | Nginx")
expertise_tree.add("📦 MySQL | Docker | Redis")
tree.add("🧹 Clean Coder | Building Robust, Maintainable Code")

# About Panel
about_content = """
I'm a passionate software engineer driven by innovation, security, and Web3.  
I build tools to strengthen systems without disrupting what supports them.

🌟 [green]Follow me on Twitter: [bold link=https://twitter.com/tal7aouy]@tal7aouy[/]
"""

about_panel = Panel.fit(
    about_content,
    box=box.DOUBLE,
    border_style="blue",
    title="[b]👋 Welcome",
    width=50,
)

# Display Content
console.print(Columns([about_panel, tree]))

# Save Output as HTML
CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
