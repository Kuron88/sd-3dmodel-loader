import gradio as gr

import modules.scripts as scripts
from modules import script_callbacks
from modules import shared
from modules.shared import opts

class Script(scripts.Script):
    def __init__(self) -> None:
        super().__init__()

    def title(self):
        return "3D Model Loader"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        return ()

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as threeDModel_loader:
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    has_ground_page = gr.Checkbox(label="Ground", value=opts.threeDmodel_has_ground)
                    has_axis_page = gr.Checkbox(label="Axis", value=opts.threeDmodel_has_axis)
                    width_page = gr.Textbox(label="Width", value=opts.threeDmodel_canvas_width)
                    height_page = gr.Textbox(label="Height", value=opts.threeDmodel_canvas_height)
                    color_page = gr.Textbox(label="Background Color", value=opts.threeDmodel_bg_color)
                with gr.Row():
                    set_canvas_button = gr.Button(value="Set Canvas")
                with gr.Row():
                    model_scale_page = gr.Textbox(label="Scale", value="1")
                with gr.Row():
                    update_model_button = gr.Button(value="Update Model")

                with gr.Row():
                    reset_btn = gr.Button(value="Reset")
                with gr.Row():
                    upload_button = gr.Button(value="Upload Model")
                    send_t2t = gr.Button(value="Send to txt2img")
                    send_i2i = gr.Button(value="Send to img2img")
                    select_target_index = gr.Dropdown([str(i) for i in range(opts.control_net_max_models_num)],
                                                      label="Send to", value="0", interactive=True,
                                                      visible=(opts.control_net_max_models_num > 1))
                with gr.Row():
                    play_pause_button = gr.Button(value="Play/Pause")
                    stop_button = gr.Button(value="Stop")

            with gr.Column():
                canvas_width = opts.threeDmodel_canvas_width + "px"
                canvas_height = opts.threeDmodel_canvas_height + "px"

                gr.HTML('<div id="WebGL-output" canvas_width="' + opts.threeDmodel_canvas_width +
                        '" canvas_height="' + opts.threeDmodel_canvas_height + '" canvas_bg_color="' +
                        opts.threeDmodel_bg_color + '" has_ground="' + str(opts.threeDmodel_has_ground) + '" has_axis="' +
                        str(opts.threeDmodel_has_axis) + '" style="width: ' +
                        canvas_width + '; height: ' + canvas_height + '; border-radius: 0.25rem; border: 0.5px solid"></div>')

        update_model_button.click(None, [model_scale_page], None, _js="(modelScalePage) => {updateModel(modelScalePage)}")
        set_canvas_button.click(None, [has_ground_page, has_axis_page, width_page, height_page, color_page], None,
                                _js="(hasGroundPage, hasAxisPage, widthPage, heightPage, colorPage) => "
                                    "{setCanvasPage(hasGroundPage, hasAxisPage, widthPage, heightPage, colorPage)}")
        play_pause_button.click(None, [], None, _js="playAndPause")
        stop_button.click(None, [], None, _js="stop")
        send_t2t.click(None, select_target_index, None, _js="(i) => {getWebGLOutputScreenshot('txt2img', i)}")
        send_i2i.click(None, select_target_index, None, _js="(i) => {getWebGLOutputScreenshot('img2img', i)}")
        reset_btn.click(None, [], None, _js="restCanvasAndCamera")
        upload_button.click(None, None, None, _js="uploadFile")

    return [(threeDModel_loader, "3d Model Loader", "3dmodel_loador")]

def on_ui_settings():
    section = ('3dmodel', "3D Model")
    shared.opts.add_option("threeDmodel_bg_color", shared.OptionInfo(
        "white", "Canvas Background Color", section=section))
    shared.opts.add_option("threeDmodel_canvas_width", shared.OptionInfo(
        "512", "Canvas Width", section=section))
    shared.opts.add_option("threeDmodel_canvas_height", shared.OptionInfo(
        "512", "Canvas Height", section=section))
    shared.opts.add_option("threeDmodel_has_ground", shared.OptionInfo(
        True, "Has Ground", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("threeDmodel_has_axis", shared.OptionInfo(
        True, "Has Axis", gr.Checkbox, {"interactive": True}, section=section))

script_callbacks.on_ui_tabs(on_ui_tabs)
script_callbacks.on_ui_settings(on_ui_settings)
