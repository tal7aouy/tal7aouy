from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

# Initialize Console
console = Console(record=True, width=120)

# Build Expertise Tree
tree = Tree("🤓 [link=https://www.talhaouy.me]Mhammed Talhaouy", guide_style="bold cyan")
expertise_tree = tree.add("💻 Senior Software Engineer | Web3 & Security Enthusiast", guide_style="bold green")

# Add technical expertise
expertise_tree.add("🐘 PHP | Laravel Specialist")
expertise_tree.add("🚀 Node.js | Vue.js")
expertise_tree.add("🧠 LangChain | PyTorch | Pandas | NumPy")
expertise_tree.add("🛠️ Solidity | Blockchain & Smart Contracts")
expertise_tree.add("☁️ AWS | CI/CD Pipelines | Nginx")
expertise_tree.add("📦 MySQL | Docker | Redis")

# Highlight coding philosophy
tree.add("🧹 Clean Coder | Building Robust, Maintainable Code")

# About Section
about_content = """
I'm a passionate software engineer who thrives on building innovative solutions, securing systems, 
and exploring the world of Web3. I enjoy creating tools that break things to make systems stronger, 
but never break what helps build — that's just unfair. 

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

# Save the output as HTML
CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""
console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
