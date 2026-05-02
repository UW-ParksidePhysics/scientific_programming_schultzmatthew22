import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os


def parse_animation_code(code_filename):
    if not os.path.exists(code_filename):
        return ["Error: animation_exercise.py not found."]

    with open(code_filename, 'r') as f:
        full_code = f.read()

    snippets = []
    parts = full_code.split('def ')
    snippets.append(parts[0].strip())
    for part in parts[1:]:
        snippets.append("def " + part.strip())

    return snippets


def format_section_header(header_string):
    h1_tag_open = "<h1>"
    h1_tag_close = "</h1>"
    return f"{h1_tag_open}{header_string}{h1_tag_close}\n"


def write_html_report(report_string, report_filename):
    with open(report_filename, 'w') as f:
        f.write(report_string)
    print(f"Report generated: {report_filename}")

def generate_assets():

    G_CONST = 9.81
    initial_conditions = [
        {'y0': 0, 'v0': 20, 'angle': 45},
        {'y0': 10, 'v0': 15, 'angle': 30},
        {'y0': 5, 'v0': 25, 'angle': 60}
    ]

    colors = ['b', 'g', 'r']
    t_max = 4.5
    t_unified = np.linspace(0, t_max, 300)

    time_steps = [1, 150, 299]
    filenames = ['plot_1.png', 'plot_2.png', 'plot_3.png']

    for i, step in enumerate(time_steps):
        fig, ax = plt.subplots(figsize=(8, 5))
        for j, cond in enumerate(initial_conditions):
            angle_rad = np.radians(cond['angle'])
            vx0 = cond['v0'] * np.cos(angle_rad)
            vy0 = cond['v0'] * np.sin(angle_rad)

            t_slice = t_unified[:step + 1]
            x = vx0 * t_slice
            y = cond['y0'] + vy0 * t_slice - 0.5 * G_CONST * t_slice ** 2
            y = np.maximum(y, 0)

            ax.plot(x, y, color=colors[j], label=f"Case {j + 1}")
            ax.plot(x[-1], y[-1], color=colors[j], marker='o')

        ax.set_title(f"Trajectory State at Frame {step}")
        ax.set_xlim(0, 60)
        ax.set_ylim(0, 30)
        ax.legend()
        plt.savefig(filenames[i])
        plt.close()

    fig, ax = plt.subplots()

    def update(frame):
        ax.clear()
        ax.set_xlim(0, 60)
        ax.set_ylim(0, 30)
        for j, cond in enumerate(initial_conditions):
            angle_rad = np.radians(cond['angle'])
            x = cond['v0'] * np.cos(angle_rad) * t_unified[:frame]
            y = cond['y0'] + (cond['v0'] * np.sin(angle_rad) * t_unified[:frame]) - (
                        0.5 * G_CONST * t_unified[:frame] ** 2)
            ax.plot(x, np.maximum(y, 0), color=colors[j])

    ani = animation.FuncAnimation(fig, update, frames=range(0, 300, 10))
    ani.save('movie.gif', writer='pillow')
    plt.close()

if __name__ == "__main__":
    generate_assets()

    CODE_FILE = 'animation_exercise.py'
    REPORT_FILE = 'animation_report.html'

    html_start = "<html>\n<head><title>Animation Report</title></head>\n<body style='padding:50px; font-family:sans-serif;'>\n"
    html_end = "</body>\n</html>"
    pre_tag_open = "<pre style='background:#eee; padding:15px; border:1px solid #ccc;'>"
    pre_tag_close = "</pre>"
    image_template = "<div style='margin:20px 0;'><img src='{src}' width='600'><br><i>{caption}</i></div>"

    content = html_start

    content += format_section_header("Program Source Code Snippets")
    snippets = parse_animation_code(CODE_FILE)
    for snippet in snippets:
        content += pre_tag_open + snippet + pre_tag_close

    content += format_section_header("System States at Different Times")
    content += image_template.format(src="plot_1.png", caption="Initial state (t=0)")
    content += image_template.format(src="plot_2.png", caption="Mid-flight state")
    content += image_template.format(src="plot_3.png", caption="Final landing state")

    content += format_section_header("Full Trajectory Animation")
    content += image_template.format(src="movie.gif", caption="Complete simulation movie")

    content += html_end

    write_html_report(content, REPORT_FILE)