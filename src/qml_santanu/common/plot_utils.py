import matplotlib.pyplot as plt

_COLORS = ['#4a90d9', '#e07b39', '#5cb85c', '#d9534f', '#9b59b6', '#1abc9c']


def plot_counts(counts, title='Histograma de mediciones'):
    """Grafica un histograma de conteos de medición cuántica.

    Acepta dicts con keys enteros (Cirq) o strings (Qiskit).
    """
    counts = {str(k): v for k, v in counts.items()}
    etiquetas = sorted(counts.keys())
    valores = [counts[k] for k in etiquetas]
    etiquetas_display = [f'|{k}⟩' for k in etiquetas]

    titulo = f'{title} ({sum(valores)} disparos)'

    fig, ax = plt.subplots(figsize=(4, 3))
    barras = ax.bar(
        etiquetas_display, valores,
        color=_COLORS[:len(valores)],
        edgecolor='white', linewidth=1.2, width=0.5,
    )

    margen = max(valores) * 0.03
    for barra, v in zip(barras, valores):
        ax.text(
            barra.get_x() + barra.get_width() / 2,
            barra.get_height() + margen,
            str(v), ha='center', va='bottom', fontsize=11,
        )

    ax.set_xlabel('Estado medido', fontsize=11)
    ax.set_ylabel('Conteo', fontsize=11)
    ax.set_title(titulo, fontsize=11)
    ax.set_ylim(0, max(valores) * 1.18)
    ax.spines[['top', 'right']].set_visible(False)
    plt.tight_layout()
    plt.show()
