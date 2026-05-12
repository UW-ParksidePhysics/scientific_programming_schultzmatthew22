import matplotlib.pyplot as plt
from datetime import datetime


def annotate_plot(annotations):
    objs = []
    for label, params in annotations.items():
        for key in ['position', 'alignment', 'fontsize']:
            if key not in params:
                raise KeyError(f"Missing required key '{key}' in annotation for '{label}'")

        obj = plt.text(
            params['position'][0], params['position'][1],
            label,
            ha=params['alignment'][0],
            va=params['alignment'][1],
            fontsize=params['fontsize'],
            transform=plt.gcf().transFigure
        )
        objs.append(obj)
    return objs


if __name__ == "__main__":
    plt.plot([0, 1], [0, 1])
    today = datetime.now().strftime('%Y-%m-%d')
    note = f"Created by Your Name {today}"
    ann = {
        note: {
            'position': [0.1, 0.02],
            'alignment': ('left', 'bottom'),
            'fontsize': 9
        }
    }
    annotate_plot(ann)
    plt.show()
#