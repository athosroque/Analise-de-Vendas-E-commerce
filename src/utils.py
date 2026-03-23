"""
Utility functions for E-commerce Sales Analysis Portfolio.
Contains styling configurations and plot saving logic.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pathlib import Path
from typing import Optional

def setup_style() -> None:
    """Configura o estilo visual padrão para os gráficos do portfólio."""
    plt.style.use('seaborn-v0_8-whitegrid')
    sns.set_palette('husl')
    mpl.rcParams.update({
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'font.size': 12,
        'axes.titlesize': 14,
        'axes.titleweight': 'bold',
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 11,
        'figure.titlesize': 16,
        'lines.linewidth': 2,
    })
    print("✓ Estilo visual do portfólio configurado.")

def save_fig(fig: mpl.figure.Figure, name: str, dpi: int = 150) -> None:
    """
    Salva a figura no diretório reports/figures com padronização visual.
    Detecta automaticamente o diretório raiz do projeto.
    
    Args:
        fig: Objeto de figura do Matplotlib.
        name: Nome do arquivo (sem extensão).
        dpi: Resolução da imagem (padrão 150).
    """
    # Resolve o caminho absoluto baseado na localização deste arquivo (src/utils.py)
    root_dir = Path(__file__).parent.parent
    out_dir = root_dir / 'reports' / 'figures'
    out_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = out_dir / f"{name}.png"
    
    fig.savefig(
        file_path,
        dpi=dpi,
        bbox_inches='tight',
        facecolor='white',
        edgecolor='none'
    )
    print(f"✓ Figura salva: {file_path.name}")
