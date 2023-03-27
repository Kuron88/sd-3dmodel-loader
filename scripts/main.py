import gradio as gr

import modules.scripts as scripts
from modules import script_callbacks
from modules import shared
from modules.shared import opts
from modules import extensions

import os


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
                with gr.Accordion("Pose", open=False):
                    with gr.Row():
                        load_pose_button = gr.Button(value="Load Pose Model", variant="primary")
                    with gr.Accordion("Body", open=False):
                        with gr.Row():
                            neck_x_page = gr.Slider(
                                label="Neck X", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_neck_x")
                            neck_y_page = gr.Slider(
                                label="Neck Y", minimum=-0.3, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_neck_y")
                            neck_z_page = gr.Slider(
                                label="Neck Z", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_neck_z")
                        with gr.Row():
                            spine_x_page = gr.Slider(
                                label="Spine X", minimum=-0.1, maximum=0.5, value=0, step=0.01, interactive=True, elem_id="pose_spine_x")
                            spine_y_page = gr.Slider(
                                label="Spine Y", minimum=-0.3, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_spine_y")
                            spine_z_page = gr.Slider(
                                label="Spine Z", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_spine_z")
                    with gr.Accordion("Left Arm", open=False):
                        with gr.Row():
                            left_upper_arm_x_page = gr.Slider(
                                label="LeftUpperArm X", minimum=-0.3, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_leftUpperArm_x")
                            left_upper_arm_y_page = gr.Slider(
                                label="LeftUpperArm Y", minimum=-0.5, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_leftUpperArm_y")
                            left_upper_arm_z_page = gr.Slider(
                                label="LeftUpperArm Z", minimum=-0.4, maximum=0.4, value=0, step=0.01, interactive=True, elem_id="pose_leftUpperArm_z")
                        with gr.Row():
                            left_lower_arm_x_page = gr.Slider(
                                label="LeftLowerArm X", minimum=-0.3, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_leftLowerArm_x")
                            left_lower_arm_y_page = gr.Slider(
                                label="LeftLowerArm Y", minimum=-0.5, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_leftLowerArm_y")
                            left_lower_arm_z_page = gr.Slider(
                                label="LeftLowerArm Z", minimum=-0.4, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_leftLowerArm_z")
                        with gr.Row():
                            left_hand_x_page = gr.Slider(
                                label="LeftHand X", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_leftHand_x")
                            left_hand_y_page = gr.Slider(
                                label="LeftHand Y", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_leftHand_y")
                            left_hand_z_page = gr.Slider(
                                label="LeftHand Z", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_leftHand_z")

                    with gr.Accordion("Right Arm", open=False):
                        with gr.Row():
                            right_upper_arm_x_page = gr.Slider(
                                label="RightUpperArm X", minimum=-0.3, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_rightUpperArm_x")
                            right_upper_arm_y_page = gr.Slider(
                                label="RightUpperArm Y", minimum=-0.5, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_rightUpperArm_y")
                            right_upper_arm_z_page = gr.Slider(
                                label="RightUpperArm Z", minimum=-0.4, maximum=0.4, value=0, step=0.01, interactive=True, elem_id="pose_rightUpperArm_z")
                        with gr.Row():
                            right_lower_arm_x_page = gr.Slider(
                                label="RightLowerArm X", minimum=-0.3, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_rightLowerArm_x")
                            right_lower_arm_y_page = gr.Slider(
                                label="RightLowerArm Y", minimum=-0.5, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_rightLowerArm_y")
                            right_lower_arm_z_page = gr.Slider(
                                label="RightLowerArm Z", minimum=-0.4, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_rightLowerArm_z")
                        with gr.Row():
                            right_hand_x_page = gr.Slider(
                                label="RightHand X", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_rightHand_x")
                            right_hand_y_page = gr.Slider(
                                label="RightHand Y", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_rightHand_y")
                            right_hand_z_page = gr.Slider(
                                label="RightHand Z", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_rightHand_z")

                    with gr.Accordion("Left Leg", open=False):
                        with gr.Row():
                            left_upper_leg_x_page = gr.Slider(
                                label="LeftUpperLeg X", minimum=-0.5, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_leftUpperLeg_x")
                            left_upper_leg_y_page = gr.Slider(
                                label="LeftUpperLeg Y", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_leftUpperLeg_y")
                            left_upper_leg_z_page = gr.Slider(
                                label="LeftUpperLeg Z", minimum=-0.1, maximum=0.6, value=0, step=0.01, interactive=True, elem_id="pose_leftUpperLeg_z")
                        with gr.Row():
                            left_lower_leg_x_page = gr.Slider(
                                label="LeftLowerLeg X", minimum=-0.05, maximum=0.7, value=0, step=0.01, interactive=True, elem_id="pose_leftLowerLeg_x")
                            left_lower_leg_y_page = gr.Slider(
                                label="LeftLowerLeg Y", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_leftLowerLeg_y")
                            left_lower_leg_z_page = gr.Slider(
                                label="LeftLowerLeg Z", minimum=-0.05, maximum=0.05, value=0, step=0.01, interactive=True, elem_id="pose_leftLowerLeg_z")
                        with gr.Row():
                            left_foot_x_page = gr.Slider(
                                label="LeftFoot X", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_leftFoot_x")
                            left_foot_y_page = gr.Slider(
                                label="LeftFoot Y", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_leftFoot_y")
                            left_foot_z_page = gr.Slider(
                                label="LeftFoot Z", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_leftFoot_z")

                    with gr.Accordion("Right Leg", open=False):
                        with gr.Row():
                            right_upper_leg_x_page = gr.Slider(
                                label="RightUpperLeg X", minimum=-0.5, maximum=0.3, value=0, step=0.01, interactive=True, elem_id="pose_rightUpperLeg_x")
                            right_upper_leg_y_page = gr.Slider(
                                label="RightUpperLeg Y", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_rightUpperLeg_y")
                            right_upper_leg_z_page = gr.Slider(
                                label="RightUpperLeg Z", minimum=-0.1, maximum=0.6, value=0, step=0.01, interactive=True, elem_id="pose_rightUpperLeg_z")

                        with gr.Row():
                            right_lower_leg_x_page = gr.Slider(
                                label="RightLowerLeg X", minimum=-0.05, maximum=0.7, value=0, step=0.01, interactive=True, elem_id="pose_rightLowerLeg_x")
                            right_lower_leg_y_page = gr.Slider(
                                label="RightLowerLeg Y", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_rightLowerLeg_y")
                            right_lower_leg_z_page = gr.Slider(
                                label="RightLowerLeg Z", minimum=-0.05, maximum=0.05, value=0, step=0.01, interactive=True, elem_id="pose_rightLowerLeg_z")

                        with gr.Row():
                            right_foot_x_page = gr.Slider(
                                label="RightFoot X", minimum=-0.2, maximum=0.2, value=0, step=0.01, interactive=True, elem_id="pose_rightFoot_x")
                            right_foot_y_page = gr.Slider(
                                label="RightFoot Y", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_rightFoot_y")
                            right_foot_z_page = gr.Slider(
                                label="RightFoot Z", minimum=-0.1, maximum=0.1, value=0, step=0.01, interactive=True, elem_id="pose_rightFoot_z")

                    with gr.Accordion("Left Hand", open=False):
                        with gr.Accordion("Thumb", open=False):
                            with gr.Row():
                                left_thumb_metacarpal_x_page = gr.Slider(
                                    label="LeftThumbMetacarpal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True, elem_id="pose_leftThumbMetacarpal_x")
                                left_thumb_metacarpal_y_page = gr.Slider(
                                    label="LeftThumbMetacarpal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True, elem_id="pose_leftThumbMetacarpal_y")
                                left_thumb_metacarpal_z_page = gr.Slider(
                                    label="LeftThumbMetacarpal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True, elem_id="pose_leftThumbMetacarpal_z")
                            with gr.Row():
                                left_thumb_proximal_x_page = gr.Slider(
                                    label="LeftThumbProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftThumbProximal_x")
                                left_thumb_proximal_y_page = gr.Slider(
                                    label="LeftThumbProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftThumbProximal_y")
                                left_thumb_proximal_z_page = gr.Slider(
                                    label="LeftThumbProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftThumbProximal_z")
                            with gr.Row():
                                left_thumb_distal_x_page = gr.Slider(
                                    label="LeftThumbDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftThumbDistal_x")
                                left_thumb_distal_y_page = gr.Slider(
                                    label="LeftThumbDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftThumbDistal_y")
                                left_thumb_distal_z_page = gr.Slider(
                                    label="LeftThumbDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftThumbDistal_z")

                        with gr.Accordion("Index", open=False):
                            with gr.Row():
                                left_index_proximal_x_page = gr.Slider(
                                    label="LeftIndexProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftIndexProximal_x")
                                left_index_proximal_y_page = gr.Slider(
                                    label="LeftIndexProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftIndexProximal_y")
                                left_index_proximal_z_page = gr.Slider(
                                    label="LeftIndexProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftIndexProximal_z")
                            with gr.Row():
                                left_index_intermediate_x_page = gr.Slider(
                                    label="LeftIndexIntermediate X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftIndexIntermediate_x")
                                left_index_intermediate_y_page = gr.Slider(
                                    label="LeftIndexIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftIndexIntermediate_y")
                                left_index_intermediate_z_page = gr.Slider(
                                    label="LeftIndexIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftIndexIntermediate_z")
                            with gr.Row():
                                left_index_distal_x_page = gr.Slider(
                                    label="LeftIndexDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftIndexDistal_x")
                                left_index_distal_y_page = gr.Slider(
                                    label="LeftIndexDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftIndexDistal_y")
                                left_index_distal_z_page = gr.Slider(
                                    label="LeftIndexDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftIndexDistal_z")

                        with gr.Accordion("Middle", open=False):
                            with gr.Row():
                                left_middle_proximal_x_page = gr.Slider(
                                    label="LeftMiddleProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftMiddleProximal_x")
                                left_middle_proximal_y_page = gr.Slider(
                                    label="LeftMiddleProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftMiddleProximal_y")
                                left_middle_proximal_z_page = gr.Slider(
                                    label="LeftMiddleProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftMiddleProximal_z")
                            with gr.Row():
                                left_middle_intermediate_x_page = gr.Slider(
                                    label="LeftMiddleIntermediate X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftMiddleIntermediate_x")
                                left_middle_intermediate_y_page = gr.Slider(
                                    label="LeftMiddleIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftMiddleIntermediate_y")
                                left_middle_intermediate_z_page = gr.Slider(
                                    label="LeftMiddleIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftMiddleIntermediate_z")
                            with gr.Row():
                                left_middle_distal_x_page = gr.Slider(
                                    label="LeftMiddleDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftMiddleDistal_x")
                                left_middle_distal_y_page = gr.Slider(
                                    label="LeftMiddleDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftMiddleDistal_y")
                                left_middle_distal_z_page = gr.Slider(
                                    label="LeftMiddleDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftMiddleDistal_z")

                        with gr.Accordion("Ring", open=False):
                            with gr.Row():
                                left_ring_proximal_x_page = gr.Slider(
                                    label="LeftRingProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftRingProximal_x")
                                left_ring_proximal_y_page = gr.Slider(
                                    label="LeftRingProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftRingProximal_y")
                                left_ring_proximal_z_page = gr.Slider(
                                    label="LeftRingProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftRingProximal_z")
                            with gr.Row():
                                left_ring_intermediate_x_page = gr.Slider(
                                    label="LeftRingIntermediate X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftRingIntermediate_x")
                                left_ring_intermediate_y_page = gr.Slider(
                                    label="LeftRingIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftRingIntermediate_y")
                                left_ring_intermediate_z_page = gr.Slider(
                                    label="LeftRingIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_leftRingIntermediate_z")
                            with gr.Row():
                                left_ring_distal_x_page = gr.Slider(
                                    label="LeftRingDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftRingDistal_x")
                                left_ring_distal_y_page = gr.Slider(
                                    label="LeftRingDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftRingDistal_y")
                                left_ring_distal_z_page = gr.Slider(
                                    label="LeftRingDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftRingDistal_z")

                        with gr.Accordion("Little", open=False):
                            with gr.Row():
                                left_little_proximal_x_page = gr.Slider(
                                    label="LeftLittleProximal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleProximal_x")
                                left_little_proximal_y_page = gr.Slider(
                                    label="LeftLittleProximal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleProximal_y")
                                left_little_proximal_z_page = gr.Slider(
                                    label="LeftLittleProximal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleProximal_z")
                            with gr.Row():
                                left_little_intermediate_x_page = gr.Slider(
                                    label="LeftLittleIntermediate X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleIntermediate_x")
                                left_little_intermediate_y_page = gr.Slider(
                                    label="LeftLittleIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleIntermediate_y")
                                left_little_intermediate_z_page = gr.Slider(
                                    label="LeftLittleIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleIntermediate_z")
                            with gr.Row():
                                left_little_distal_x_page = gr.Slider(
                                    label="LeftLittleDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleDistal_x")
                                left_little_distal_y_page = gr.Slider(
                                    label="LeftLittleDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleDistal_y")
                                left_little_distal_z_page = gr.Slider(
                                    label="LeftLittleDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_leftLittleDistal_z")

                    with gr.Accordion("Right Hand", open=False):
                        with gr.Accordion("Thumb", open=False):
                            with gr.Row():
                                right_thumb_metacarpal_x_page = gr.Slider(
                                    label="RightThumbMetacarpal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightThumbMetacarpal_x")
                                right_thumb_metacarpal_y_page = gr.Slider(
                                    label="RightThumbMetacarpal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightThumbMetacarpal_y")
                                right_thumb_metacarpal_z_page = gr.Slider(
                                    label="RightThumbMetacarpal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightThumbMetacarpal_z")
                            with gr.Row():
                                right_thumb_proximal_x_page = gr.Slider(
                                    label="RightThumbProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightThumbProximal_x")
                                right_thumb_proximal_y_page = gr.Slider(
                                    label="RightThumbProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightThumbProximal_y")
                                right_thumb_proximal_z_page = gr.Slider(
                                    label="RightThumbProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightThumbProximal_z")
                            with gr.Row():
                                right_thumb_distal_x_page = gr.Slider(
                                    label="RightThumbDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightThumbDistal_x")
                                right_thumb_distal_y_page = gr.Slider(
                                    label="RightThumbDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightThumbDistal_y")
                                right_thumb_distal_z_page = gr.Slider(
                                    label="RightThumbDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightThumbDistal_z")

                        with gr.Accordion("Index", open=False):
                            with gr.Row():
                                right_index_proximal_x_page = gr.Slider(
                                    label="RightIndexProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightIndexProximal_x")
                                right_index_proximal_y_page = gr.Slider(
                                    label="RightIndexProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightIndexProximal_y")
                                right_index_proximal_z_page = gr.Slider(
                                    label="RightIndexProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightIndexProximal_z")
                            with gr.Row():
                                right_index_intermediate_x_page = gr.Slider(
                                    label="RightIndexIntermediate X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightIndexIntermediate_x")
                                right_index_intermediate_y_page = gr.Slider(
                                    label="RightIndexIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightIndexIntermediate_y")
                                right_index_intermediate_z_page = gr.Slider(
                                    label="RightIndexIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightIndexIntermediate_z")
                            with gr.Row():
                                right_index_distal_x_page = gr.Slider(
                                    label="RightIndexDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightIndexDistal_x")
                                right_index_distal_y_page = gr.Slider(
                                    label="RightIndexDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightIndexDistal_y")
                                right_index_distal_z_page = gr.Slider(
                                    label="RightIndexDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightIndexDistal_z")

                        with gr.Accordion("Middle", open=False):
                            with gr.Row():
                                right_middle_proximal_x_page = gr.Slider(
                                    label="RightMiddleProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightMiddleProximal_x")
                                right_middle_proximal_y_page = gr.Slider(
                                    label="RightMiddleProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightMiddleProximal_y")
                                right_middle_proximal_z_page = gr.Slider(
                                    label="RightMiddleProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightMiddleProximal_z")
                            with gr.Row():
                                right_middle_intermediate_x_page = gr.Slider(
                                    label="RightMiddleIntermediate X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightMiddleIntermediate_x")
                                right_middle_intermediate_y_page = gr.Slider(
                                    label="RightMiddleIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightMiddleIntermediate_y")
                                right_middle_intermediate_z_page = gr.Slider(
                                    label="RightMiddleIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightMiddleIntermediate_z")
                            with gr.Row():
                                right_middle_distal_x_page = gr.Slider(
                                    label="RightMiddleDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightMiddleDistal_x")
                                right_middle_distal_y_page = gr.Slider(
                                    label="RightMiddleDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightMiddleDistal_y")
                                right_middle_distal_z_page = gr.Slider(
                                    label="RightMiddleDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightMiddleDistal_z")

                        with gr.Accordion("Ring", open=False):
                            with gr.Row():
                                right_ring_proximal_x_page = gr.Slider(
                                    label="RightRingProximal X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightRingProximal_x")
                                right_ring_proximal_y_page = gr.Slider(
                                    label="RightRingProximal Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightRingProximal_y")
                                right_ring_proximal_z_page = gr.Slider(
                                    label="RightRingProximal Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightRingProximal_z")
                            with gr.Row():
                                right_ring_intermediate_x_page = gr.Slider(
                                    label="RightRingIntermediate X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightRingIntermediate_x")
                                right_ring_intermediate_y_page = gr.Slider(
                                    label="RightRingIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightRingIntermediate_y")
                                right_ring_intermediate_z_page = gr.Slider(
                                    label="RightRingIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True,
                                    elem_id="pose_rightRingIntermediate_z")
                            with gr.Row():
                                right_ring_distal_x_page = gr.Slider(
                                    label="RightRingDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightRingDistal_x")
                                right_ring_distal_y_page = gr.Slider(
                                    label="RightRingDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightRingDistal_y")
                                right_ring_distal_z_page = gr.Slider(
                                    label="RightRingDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightRingDistal_z")

                        with gr.Accordion("Little", open=False):
                            with gr.Row():
                                right_little_proximal_x_page = gr.Slider(
                                    label="RightLittleProximal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleProximal_x")
                                right_little_proximal_y_page = gr.Slider(
                                    label="RightLittleProximal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleProximal_y")
                                right_little_proximal_z_page = gr.Slider(
                                    label="RightLittleProximal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleProximal_z")
                            with gr.Row():
                                right_little_intermediate_x_page = gr.Slider(
                                    label="RightLittleIntermediate X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleIntermediate_x")
                                right_little_intermediate_y_page = gr.Slider(
                                    label="RightLittleIntermediate Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleIntermediate_y")
                                right_little_intermediate_z_page = gr.Slider(
                                    label="RightLittleIntermediate Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleIntermediate_z")
                            with gr.Row():
                                right_little_distal_x_page = gr.Slider(
                                    label="RightLittleDistal X", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleDistal_x")
                                right_little_distal_y_page = gr.Slider(
                                    label="RightLittleDistal Y", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleDistal_y")
                                right_little_distal_z_page = gr.Slider(
                                    label="RightLittleDistal Z", minimum=-1, maximum=1, value=0, step=0.01,
                                    interactive=True,
                                    elem_id="pose_rightLittleDistal_z")


                    with gr.Row():
                        save_pose_as_json_button = gr.Button(value="Save Pose as json")
                        load_pose_from_json_button = gr.Button(value="Load Pose from json")
                with gr.Accordion("Canvas", open=False):
                    with gr.Row():
                        with gr.Column():
                            width_page = gr.Slider(label="Width", minimum=64, maximum=2048, value=512, step=64,
                                                   interactive=True)
                            height_page = gr.Slider(label="Height", minimum=64, maximum=2048, value=512, step=64,
                                                    interactive=True)
                        with gr.Column():
                            light_position_x_page = gr.Slider(
                                label="Light Position X", minimum=-100, maximum=100, value=0, step=1, interactive=True)
                            light_position_y_page = gr.Slider(
                                label="Light Position Y", minimum=0, maximum=100, value=30, step=1, interactive=True)
                            light_position_z_page = gr.Slider(
                                label="Light Position Z", minimum=-100, maximum=100, value=0, step=1, interactive=True)
                    with gr.Row():
                        has_ground_page = gr.Checkbox(label="Show Ground", value=opts.threeDmodel_has_ground)
                        has_ground_grid_page = gr.Checkbox(label="Show Grid", value=opts.threeDmodel_has_ground_grid)
                        has_axis_page = gr.Checkbox(label="Show Axis", value=opts.threeDmodel_has_axis)
                        with gr.Row():
                            color_page = gr.ColorPicker(label="Background Color", value=opts.threeDmodel_bg_color,
                                                        elem_id="bg_color")
                            ground_color_page = gr.ColorPicker(label="Ground Color",
                                                               value=opts.threeDmodel_ground_color,
                                                               elem_id="ground_color")
                            light_color_page = gr.ColorPicker(label="Light Color", value=opts.threeDmodel_ground_color,
                                                              elem_id="Light_color")
                with gr.Accordion("Model", open=False):
                    with gr.Row():
                        model_scale_page = gr.Slider(label="Scale", minimum=0.01, maximum=10, step=0.01, value=1)
                    with gr.Row():
                        model_rotate_x_page = gr.Slider(
                            label="Rotate X", minimum=-1, maximum=1, value=0, step=0.01, interactive=True)
                        model_rotate_y_page = gr.Slider(
                            label="Rotate Y", minimum=-1, maximum=1, value=0, step=0.01, interactive=True)
                        model_rotate_z_page = gr.Slider(
                            label="Rotate Z", minimum=-1, maximum=1, value=0, step=0.01, interactive=True)

                with gr.Row():
                    upload_button = gr.Button(value="Load Model", variant="primary")
                with gr.Accordion("Upload Settings", open=False):
                    with gr.Row():
                        multi_files_checkbox = gr.Checkbox(label="includes additional resource(multi files select)")
                        entry_type = gr.Dropdown(["vrm"], label="Entry Type", interactive=True, visible=True)
                    with gr.Row():
                        gr.HTML("<div>Notice, currently multi files select only supports VRM models combine with FBX "
                                "animation from Mixamo, other formats support will add later </div>")

                with gr.Row():
                    reset_btn = gr.Button(value="Reset")
                    send_t2t = gr.Button(value="Send to txt2img")
                    send_i2i = gr.Button(value="Send to img2img")

                    try:
                        control_net_num = opts.control_net_max_models_num
                    except:
                        control_net_num = 1

                    select_target_index = gr.Dropdown([str(i) for i in range(control_net_num)],
                                                      label="Send to", value="0", interactive=True,
                                                      visible=(control_net_num > 1))


                with gr.Accordion("Animation", open=False):
                    with gr.Row():
                        play_pause_button = gr.Button(value="Play/Pause")
                        stop_button = gr.Button(value="Stop")
                    with gr.Row():
                        progress_bar = gr.Slider(label="Progress", minimum=0, maximum=100, value=0, step=0.5,
                                                 interactive=True, elem_id="progress_bar_3dmodel")

            with gr.Column():
                gr.HTML(
                    f'<div id="WebGL-output-3dmodel" canvas_width="{opts.threeDmodel_canvas_width}" canvas_height="{opts.threeDmodel_canvas_height}" ' +
                    f'canvas_bg_color="{opts.threeDmodel_bg_color}" canvas_ground_color="{opts.threeDmodel_ground_color}" ' +
                    f'has_ground="{opts.threeDmodel_has_ground}" has_ground_grid="{opts.threeDmodel_has_ground_grid}" has_axis="{opts.threeDmodel_has_axis}" ' +
                    f'style="width: {int(opts.threeDmodel_canvas_width) + 2}px; height: {int(opts.threeDmodel_canvas_height) + 2}px; border: 0.5px solid;"></div>')

                import_id = 'WebGL-output-3dmodel-import'

                ext = get_self_extension()
                if ext is None:
                    return []
                js_ = [f'{x.path}?{os.path.getmtime(x.path)}' for x in ext.list_files('javascript/lazyload', '.js')]
                js_.insert(0, ext.path)

                gr.HTML(value='\n'.join(js_), elem_id=import_id, visible=False)

        right_little_proximal_x_page.change(None, [right_little_proximal_x_page, right_little_proximal_y_page,
                                                  right_little_proximal_z_page],
                                           None,
                                           _js="poseRotateRightLittleProximal3DModel")
        right_little_proximal_y_page.change(None, [right_little_proximal_x_page, right_little_proximal_y_page,
                                                  right_little_proximal_z_page],
                                           None,
                                           _js="poseRotateRightLittleProximal3DModel")
        right_little_proximal_z_page.change(None, [right_little_proximal_x_page, right_little_proximal_y_page,
                                                  right_little_proximal_z_page],
                                           None,
                                           _js="poseRotateRightLittleProximal3DModel")

        right_little_intermediate_x_page.change(None, [right_little_intermediate_x_page, right_little_intermediate_y_page,
                                                      right_little_intermediate_z_page],
                                               None,
                                               _js="poseRotateRightLittleIntermediate3DModel")
        right_little_intermediate_y_page.change(None, [right_little_intermediate_x_page, right_little_intermediate_y_page,
                                                      right_little_intermediate_z_page],
                                               None,
                                               _js="poseRotateRightLittleIntermediate3DModel")
        right_little_intermediate_z_page.change(None, [right_little_intermediate_x_page, right_little_intermediate_y_page,
                                                      right_little_intermediate_z_page],
                                               None,
                                               _js="poseRotateRightLittleIntermediate3DModel")

        right_little_distal_x_page.change(None, [right_little_distal_x_page, right_little_distal_y_page,
                                                right_little_distal_z_page],
                                         None,
                                         _js="poseRotateRightLittleDistal3DModel")
        right_little_distal_y_page.change(None, [right_little_distal_x_page, right_little_distal_y_page,
                                                right_little_distal_z_page],
                                         None,
                                         _js="poseRotateRightLittleDistal3DModel")
        right_little_distal_z_page.change(None, [right_little_distal_x_page, right_little_distal_y_page,
                                                right_little_distal_z_page],
                                         None,
                                         _js="poseRotateRightLittleDistal3DModel")

        right_ring_proximal_x_page.change(None, [right_ring_proximal_x_page, right_ring_proximal_y_page,
                                                right_ring_proximal_z_page],
                                         None,
                                         _js="poseRotateRightRingProximal3DModel")
        right_ring_proximal_y_page.change(None, [right_ring_proximal_x_page, right_ring_proximal_y_page,
                                                right_ring_proximal_z_page],
                                         None,
                                         _js="poseRotateRightRingProximal3DModel")
        right_ring_proximal_z_page.change(None, [right_ring_proximal_x_page, right_ring_proximal_y_page,
                                                right_ring_proximal_z_page],
                                         None,
                                         _js="poseRotateRightRingProximal3DModel")

        right_ring_intermediate_x_page.change(None, [right_ring_intermediate_x_page, right_ring_intermediate_y_page,
                                                    right_ring_intermediate_z_page],
                                             None,
                                             _js="poseRotateRightRingIntermediate3DModel")
        right_ring_intermediate_y_page.change(None, [right_ring_intermediate_x_page, right_ring_intermediate_y_page,
                                                    right_ring_intermediate_z_page],
                                             None,
                                             _js="poseRotateRightRingIntermediate3DModel")
        right_ring_intermediate_z_page.change(None, [right_ring_intermediate_x_page, right_ring_intermediate_y_page,
                                                    right_ring_intermediate_z_page],
                                             None,
                                             _js="poseRotateRightRingIntermediate3DModel")

        right_ring_distal_x_page.change(None, [right_ring_distal_x_page, right_ring_distal_y_page,
                                              right_ring_distal_z_page],
                                       None,
                                       _js="poseRotateRightRingDistal3DModel")
        right_ring_distal_y_page.change(None, [right_ring_distal_x_page, right_ring_distal_y_page,
                                              right_ring_distal_z_page],
                                       None,
                                       _js="poseRotateRightRingDistal3DModel")
        right_ring_distal_z_page.change(None, [right_ring_distal_x_page, right_ring_distal_y_page,
                                              right_ring_distal_z_page],
                                       None,
                                       _js="poseRotateRightRingDistal3DModel")

        right_middle_proximal_x_page.change(None, [right_middle_proximal_x_page, right_middle_proximal_y_page,
                                                  right_middle_proximal_z_page],
                                           None,
                                           _js="poseRotateRightMiddleProximal3DModel")
        right_middle_proximal_y_page.change(None, [right_middle_proximal_x_page, right_middle_proximal_y_page,
                                                  right_middle_proximal_z_page],
                                           None,
                                           _js="poseRotateRightMiddleProximal3DModel")
        right_middle_proximal_z_page.change(None, [right_middle_proximal_x_page, right_middle_proximal_y_page,
                                                  right_middle_proximal_z_page],
                                           None,
                                           _js="poseRotateRightMiddleProximal3DModel")

        right_middle_intermediate_x_page.change(None, [right_middle_intermediate_x_page, right_middle_intermediate_y_page,
                                                      right_middle_intermediate_z_page],
                                               None,
                                               _js="poseRotateRightMiddleIntermediate3DModel")
        right_middle_intermediate_y_page.change(None, [right_middle_intermediate_x_page, right_middle_intermediate_y_page,
                                                      right_middle_intermediate_z_page],
                                               None,
                                               _js="poseRotateRightMiddleIntermediate3DModel")
        right_middle_intermediate_z_page.change(None, [right_middle_intermediate_x_page, right_middle_intermediate_y_page,
                                                      right_middle_intermediate_z_page],
                                               None,
                                               _js="poseRotateRightMiddleIntermediate3DModel")

        right_middle_distal_x_page.change(None, [right_middle_distal_x_page, right_middle_distal_y_page,
                                                right_middle_distal_z_page],
                                         None,
                                         _js="poseRotateRightMiddleDistal3DModel")
        right_middle_distal_y_page.change(None, [right_middle_distal_x_page, right_middle_distal_y_page,
                                                right_middle_distal_z_page],
                                         None,
                                         _js="poseRotateRightMiddleDistal3DModel")
        right_middle_distal_z_page.change(None, [right_middle_distal_x_page, right_middle_distal_y_page,
                                                right_middle_distal_z_page],
                                         None,
                                         _js="poseRotateRightMiddleDistal3DModel")

        right_index_proximal_x_page.change(None, [right_index_proximal_x_page, right_index_proximal_y_page,
                                                 right_index_proximal_z_page],
                                          None,
                                          _js="poseRotateRightIndexProximal3DModel")
        right_index_proximal_y_page.change(None, [right_index_proximal_x_page, right_index_proximal_y_page,
                                                 right_index_proximal_z_page],
                                          None,
                                          _js="poseRotateRightIndexProximal3DModel")
        right_index_proximal_z_page.change(None, [right_index_proximal_x_page, right_index_proximal_y_page,
                                                 right_index_proximal_z_page],
                                          None,
                                          _js="poseRotateRightIndexProximal3DModel")

        right_index_intermediate_x_page.change(None, [right_index_intermediate_x_page, right_index_intermediate_y_page,
                                                     right_index_intermediate_z_page],
                                              None,
                                              _js="poseRotateRightIndexIntermediate3DModel")
        right_index_intermediate_y_page.change(None, [right_index_intermediate_x_page, right_index_intermediate_y_page,
                                                     right_index_intermediate_z_page],
                                              None,
                                              _js="poseRotateRightIndexIntermediate3DModel")
        right_index_intermediate_z_page.change(None, [right_index_intermediate_x_page, right_index_intermediate_y_page,
                                                     right_index_intermediate_z_page],
                                              None,
                                              _js="poseRotateRightIndexIntermediate3DModel")

        right_index_distal_x_page.change(None, [right_index_distal_x_page, right_index_distal_y_page,
                                               right_index_distal_z_page],
                                        None,
                                        _js="poseRotateRightIndexDistal3DModel")
        right_index_distal_y_page.change(None, [right_index_distal_x_page, right_index_distal_y_page,
                                               right_index_distal_z_page],
                                        None,
                                        _js="poseRotateRightIndexDistal3DModel")
        right_index_distal_z_page.change(None, [right_index_distal_x_page, right_index_distal_y_page,
                                               right_index_distal_z_page],
                                        None,
                                        _js="poseRotateRightIndexDistal3DModel")

        right_thumb_metacarpal_x_page.change(None, [right_thumb_metacarpal_x_page, right_thumb_metacarpal_y_page,
                                                   right_thumb_metacarpal_z_page],
                                            None,
                                            _js="poseRotateRightThumbMetacarpal3DModel")
        right_thumb_metacarpal_y_page.change(None, [right_thumb_metacarpal_x_page, right_thumb_metacarpal_y_page,
                                                   right_thumb_metacarpal_z_page],
                                            None,
                                            _js="poseRotateRightThumbMetacarpal3DModel")
        right_thumb_metacarpal_z_page.change(None, [right_thumb_metacarpal_x_page, right_thumb_metacarpal_y_page,
                                                   right_thumb_metacarpal_z_page],
                                            None,
                                            _js="poseRotateRightThumbMetacarpal3DModel")

        right_thumb_proximal_x_page.change(None, [right_thumb_proximal_x_page, right_thumb_proximal_y_page,
                                                 right_thumb_proximal_z_page],
                                          None,
                                          _js="poseRotateRightThumbProximal3DModel")
        right_thumb_proximal_y_page.change(None, [right_thumb_proximal_x_page, right_thumb_proximal_y_page,
                                                 right_thumb_proximal_z_page],
                                          None,
                                          _js="poseRotateRightThumbProximal3DModel")
        right_thumb_proximal_z_page.change(None, [right_thumb_proximal_x_page, right_thumb_proximal_y_page,
                                                 right_thumb_proximal_z_page],
                                          None,
                                          _js="poseRotateRightThumbProximal3DModel")

        right_thumb_distal_x_page.change(None, [right_thumb_distal_x_page, right_thumb_distal_y_page,
                                               right_thumb_distal_z_page],
                                        None,
                                        _js="poseRotateRightThumbDistal3DModel")
        right_thumb_distal_y_page.change(None, [right_thumb_distal_x_page, right_thumb_distal_y_page,
                                               right_thumb_distal_z_page],
                                        None,
                                        _js="poseRotateRightThumbDistal3DModel")
        right_thumb_distal_z_page.change(None, [right_thumb_distal_x_page, right_thumb_distal_y_page,
                                               right_thumb_distal_z_page],
                                        None,
                                        _js="poseRotateRightThumbDistal3DModel")





        left_little_proximal_x_page.change(None, [left_little_proximal_x_page, left_little_proximal_y_page,
                                                left_little_proximal_z_page],
                                         None,
                                         _js="poseRotateLeftLittleProximal3DModel")
        left_little_proximal_y_page.change(None, [left_little_proximal_x_page, left_little_proximal_y_page,
                                                left_little_proximal_z_page],
                                         None,
                                         _js="poseRotateLeftLittleProximal3DModel")
        left_little_proximal_z_page.change(None, [left_little_proximal_x_page, left_little_proximal_y_page,
                                                left_little_proximal_z_page],
                                         None,
                                         _js="poseRotateLeftLittleProximal3DModel")

        left_little_intermediate_x_page.change(None, [left_little_intermediate_x_page, left_little_intermediate_y_page,
                                                    left_little_intermediate_z_page],
                                             None,
                                             _js="poseRotateLeftLittleIntermediate3DModel")
        left_little_intermediate_y_page.change(None, [left_little_intermediate_x_page, left_little_intermediate_y_page,
                                                    left_little_intermediate_z_page],
                                             None,
                                             _js="poseRotateLeftLittleIntermediate3DModel")
        left_little_intermediate_z_page.change(None, [left_little_intermediate_x_page, left_little_intermediate_y_page,
                                                    left_little_intermediate_z_page],
                                             None,
                                             _js="poseRotateLeftLittleIntermediate3DModel")

        left_little_distal_x_page.change(None, [left_little_distal_x_page, left_little_distal_y_page,
                                              left_little_distal_z_page],
                                       None,
                                       _js="poseRotateLeftLittleDistal3DModel")
        left_little_distal_y_page.change(None, [left_little_distal_x_page, left_little_distal_y_page,
                                              left_little_distal_z_page],
                                       None,
                                       _js="poseRotateLeftLittleDistal3DModel")
        left_little_distal_z_page.change(None, [left_little_distal_x_page, left_little_distal_y_page,
                                              left_little_distal_z_page],
                                       None,
                                       _js="poseRotateLeftLittleDistal3DModel")



        left_ring_proximal_x_page.change(None, [left_ring_proximal_x_page, left_ring_proximal_y_page,
                                                  left_ring_proximal_z_page],
                                           None,
                                           _js="poseRotateLeftRingProximal3DModel")
        left_ring_proximal_y_page.change(None, [left_ring_proximal_x_page, left_ring_proximal_y_page,
                                                  left_ring_proximal_z_page],
                                           None,
                                           _js="poseRotateLeftRingProximal3DModel")
        left_ring_proximal_z_page.change(None, [left_ring_proximal_x_page, left_ring_proximal_y_page,
                                                  left_ring_proximal_z_page],
                                           None,
                                           _js="poseRotateLeftRingProximal3DModel")

        left_ring_intermediate_x_page.change(None, [left_ring_intermediate_x_page, left_ring_intermediate_y_page,
                                                      left_ring_intermediate_z_page],
                                               None,
                                               _js="poseRotateLeftRingIntermediate3DModel")
        left_ring_intermediate_y_page.change(None, [left_ring_intermediate_x_page, left_ring_intermediate_y_page,
                                                      left_ring_intermediate_z_page],
                                               None,
                                               _js="poseRotateLeftRingIntermediate3DModel")
        left_ring_intermediate_z_page.change(None, [left_ring_intermediate_x_page, left_ring_intermediate_y_page,
                                                      left_ring_intermediate_z_page],
                                               None,
                                               _js="poseRotateLeftRingIntermediate3DModel")

        left_ring_distal_x_page.change(None, [left_ring_distal_x_page, left_ring_distal_y_page,
                                                left_ring_distal_z_page],
                                         None,
                                         _js="poseRotateLeftRingDistal3DModel")
        left_ring_distal_y_page.change(None, [left_ring_distal_x_page, left_ring_distal_y_page,
                                                left_ring_distal_z_page],
                                         None,
                                         _js="poseRotateLeftRingDistal3DModel")
        left_ring_distal_z_page.change(None, [left_ring_distal_x_page, left_ring_distal_y_page,
                                                left_ring_distal_z_page],
                                         None,
                                         _js="poseRotateLeftRingDistal3DModel")




        left_middle_proximal_x_page.change(None, [left_middle_proximal_x_page, left_middle_proximal_y_page,
                                                 left_middle_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftMiddleProximal3DModel")
        left_middle_proximal_y_page.change(None, [left_middle_proximal_x_page, left_middle_proximal_y_page,
                                                 left_middle_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftMiddleProximal3DModel")
        left_middle_proximal_z_page.change(None, [left_middle_proximal_x_page, left_middle_proximal_y_page,
                                                 left_middle_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftMiddleProximal3DModel")

        left_middle_intermediate_x_page.change(None, [left_middle_intermediate_x_page, left_middle_intermediate_y_page,
                                                     left_middle_intermediate_z_page],
                                              None,
                                              _js="poseRotateLeftMiddleIntermediate3DModel")
        left_middle_intermediate_y_page.change(None, [left_middle_intermediate_x_page, left_middle_intermediate_y_page,
                                                     left_middle_intermediate_z_page],
                                              None,
                                              _js="poseRotateLeftMiddleIntermediate3DModel")
        left_middle_intermediate_z_page.change(None, [left_middle_intermediate_x_page, left_middle_intermediate_y_page,
                                                     left_middle_intermediate_z_page],
                                              None,
                                              _js="poseRotateLeftMiddleIntermediate3DModel")

        left_middle_distal_x_page.change(None, [left_middle_distal_x_page, left_middle_distal_y_page,
                                               left_middle_distal_z_page],
                                        None,
                                        _js="poseRotateLeftMiddleDistal3DModel")
        left_middle_distal_y_page.change(None, [left_middle_distal_x_page, left_middle_distal_y_page,
                                               left_middle_distal_z_page],
                                        None,
                                        _js="poseRotateLeftMiddleDistal3DModel")
        left_middle_distal_z_page.change(None, [left_middle_distal_x_page, left_middle_distal_y_page,
                                               left_middle_distal_z_page],
                                        None,
                                        _js="poseRotateLeftMiddleDistal3DModel")

        left_index_proximal_x_page.change(None, [left_index_proximal_x_page, left_index_proximal_y_page,
                                                 left_index_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftIndexProximal3DModel")
        left_index_proximal_y_page.change(None, [left_index_proximal_x_page, left_index_proximal_y_page,
                                                 left_index_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftIndexProximal3DModel")
        left_index_proximal_z_page.change(None, [left_index_proximal_x_page, left_index_proximal_y_page,
                                                 left_index_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftIndexProximal3DModel")

        left_index_intermediate_x_page.change(None, [left_index_intermediate_x_page, left_index_intermediate_y_page,
                                                   left_index_intermediate_z_page],
                                            None,
                                            _js="poseRotateLeftIndexIntermediate3DModel")
        left_index_intermediate_y_page.change(None, [left_index_intermediate_x_page, left_index_intermediate_y_page,
                                                   left_index_intermediate_z_page],
                                            None,
                                            _js="poseRotateLeftIndexIntermediate3DModel")
        left_index_intermediate_z_page.change(None, [left_index_intermediate_x_page, left_index_intermediate_y_page,
                                                   left_index_intermediate_z_page],
                                            None,
                                            _js="poseRotateLeftIndexIntermediate3DModel")

        left_index_distal_x_page.change(None, [left_index_distal_x_page, left_index_distal_y_page,
                                               left_index_distal_z_page],
                                        None,
                                        _js="poseRotateLeftIndexDistal3DModel")
        left_index_distal_y_page.change(None, [left_index_distal_x_page, left_index_distal_y_page,
                                               left_index_distal_z_page],
                                        None,
                                        _js="poseRotateLeftIndexDistal3DModel")
        left_index_distal_z_page.change(None, [left_index_distal_x_page, left_index_distal_y_page,
                                               left_index_distal_z_page],
                                        None,
                                        _js="poseRotateLeftIndexDistal3DModel")

        left_thumb_metacarpal_x_page.change(None, [left_thumb_metacarpal_x_page, left_thumb_metacarpal_y_page,
                                                   left_thumb_metacarpal_z_page],
                                            None,
                                            _js="poseRotateLeftThumbMetacarpal3DModel")
        left_thumb_metacarpal_y_page.change(None, [left_thumb_metacarpal_x_page, left_thumb_metacarpal_y_page,
                                                   left_thumb_metacarpal_z_page],
                                            None,
                                            _js="poseRotateLeftThumbMetacarpal3DModel")
        left_thumb_metacarpal_z_page.change(None, [left_thumb_metacarpal_x_page, left_thumb_metacarpal_y_page,
                                                   left_thumb_metacarpal_z_page],
                                            None,
                                            _js="poseRotateLeftThumbMetacarpal3DModel")

        left_thumb_proximal_x_page.change(None, [left_thumb_proximal_x_page, left_thumb_proximal_y_page,
                                                 left_thumb_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftThumbProximal3DModel")
        left_thumb_proximal_y_page.change(None, [left_thumb_proximal_x_page, left_thumb_proximal_y_page,
                                                 left_thumb_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftThumbProximal3DModel")
        left_thumb_proximal_z_page.change(None, [left_thumb_proximal_x_page, left_thumb_proximal_y_page,
                                                 left_thumb_proximal_z_page],
                                          None,
                                          _js="poseRotateLeftThumbProximal3DModel")

        left_thumb_distal_x_page.change(None, [left_thumb_distal_x_page, left_thumb_distal_y_page,
                                               left_thumb_distal_z_page],
                                        None,
                                        _js="poseRotateLeftThumbDistal3DModel")
        left_thumb_distal_y_page.change(None, [left_thumb_distal_x_page, left_thumb_distal_y_page,
                                               left_thumb_distal_z_page],
                                        None,
                                        _js="poseRotateLeftThumbDistal3DModel")
        left_thumb_distal_z_page.change(None, [left_thumb_distal_x_page, left_thumb_distal_y_page,
                                               left_thumb_distal_z_page],
                                        None,
                                        _js="poseRotateLeftThumbDistal3DModel")


        save_pose_as_json_button.click(None, None, None, _js='savePoseAsJson3DModel')
        load_pose_from_json_button.click(None, None, None, _js='loadPoseFromJson3DModel')

        load_pose_button.click(None, None, None, _js='loadPoseFile3DModel')

        spine_x_page.change(None, [spine_x_page, spine_y_page, spine_z_page],
                                 None,
                                 _js="poseRotateSpine3DModel")
        spine_y_page.change(None, [spine_x_page, spine_y_page, spine_z_page],
                                 None,
                                 _js="poseRotateSpine3DModel")
        spine_z_page.change(None, [spine_x_page, spine_y_page, spine_z_page],
                                 None,
                                 _js="poseRotateSpine3DModel")

        right_foot_x_page.change(None, [right_foot_x_page, right_foot_y_page, right_foot_z_page],
                                 None,
                                 _js="poseRotateRightFoot3DModel")
        right_foot_y_page.change(None, [right_foot_x_page, right_foot_y_page, right_foot_z_page],
                                 None,
                                 _js="poseRotateRightFoot3DModel")
        right_foot_z_page.change(None, [right_foot_x_page, right_foot_y_page, right_foot_z_page],
                                 None,
                                 _js="poseRotateRightFoot3DModel")

        left_foot_x_page.change(None, [left_foot_x_page, left_foot_y_page, left_foot_z_page], None,
                                _js="poseRotateLeftFoot3DModel")
        left_foot_y_page.change(None, [left_foot_x_page, left_foot_y_page, left_foot_z_page], None,
                                _js="poseRotateLeftFoot3DModel")
        left_foot_z_page.change(None, [left_foot_x_page, left_foot_y_page, left_foot_z_page], None,
                                _js="poseRotateLeftFoot3DModel")

        right_hand_x_page.change(None, [right_hand_x_page, right_hand_y_page, right_hand_z_page],
                                      None,
                                      _js="poseRotateRightHand3DModel")
        right_hand_y_page.change(None, [right_hand_x_page, right_hand_y_page, right_hand_z_page],
                                      None,
                                      _js="poseRotateRightHand3DModel")
        right_hand_z_page.change(None, [right_hand_x_page, right_hand_y_page, right_hand_z_page],
                                      None,
                                      _js="poseRotateRightHand3DModel")

        left_hand_x_page.change(None, [left_hand_x_page, left_hand_y_page, left_hand_z_page], None,
                                     _js="poseRotateLeftHand3DModel")
        left_hand_y_page.change(None, [left_hand_x_page, left_hand_y_page, left_hand_z_page], None,
                                     _js="poseRotateLeftHand3DModel")
        left_hand_z_page.change(None, [left_hand_x_page, left_hand_y_page, left_hand_z_page], None,
                                     _js="poseRotateLeftHand3DModel")

        right_lower_leg_x_page.change(None, [right_lower_leg_x_page, right_lower_leg_y_page, right_lower_leg_z_page],
                                      None,
                                      _js="poseRotateRightLowerLeg3DModel")
        right_lower_leg_y_page.change(None, [right_lower_leg_x_page, right_lower_leg_y_page, right_lower_leg_z_page],
                                      None,
                                      _js="poseRotateRightLowerLeg3DModel")
        right_lower_leg_z_page.change(None, [right_lower_leg_x_page, right_lower_leg_y_page, right_lower_leg_z_page],
                                      None,
                                      _js="poseRotateRightLowerLeg3DModel")

        left_lower_leg_x_page.change(None, [left_lower_leg_x_page, left_lower_leg_y_page, left_lower_leg_z_page], None,
                                     _js="poseRotateLeftLowerLeg3DModel")
        left_lower_leg_y_page.change(None, [left_lower_leg_x_page, left_lower_leg_y_page, left_lower_leg_z_page], None,
                                     _js="poseRotateLeftLowerLeg3DModel")
        left_lower_leg_z_page.change(None, [left_lower_leg_x_page, left_lower_leg_y_page, left_lower_leg_z_page], None,
                                     _js="poseRotateLeftLowerLeg3DModel")

        right_upper_leg_x_page.change(None, [right_upper_leg_x_page, right_upper_leg_y_page, right_upper_leg_z_page], None,
                                     _js="poseRotateRightUpperLeg3DModel")
        right_upper_leg_y_page.change(None, [right_upper_leg_x_page, right_upper_leg_y_page, right_upper_leg_z_page], None,
                                     _js="poseRotateRightUpperLeg3DModel")
        right_upper_leg_z_page.change(None, [right_upper_leg_x_page, right_upper_leg_y_page, right_upper_leg_z_page], None,
                                     _js="poseRotateRightUpperLeg3DModel")

        left_upper_leg_x_page.change(None, [left_upper_leg_x_page, left_upper_leg_y_page, left_upper_leg_z_page], None,
                                     _js="poseRotateLeftUpperLeg3DModel")
        left_upper_leg_y_page.change(None, [left_upper_leg_x_page, left_upper_leg_y_page, left_upper_leg_z_page], None,
                                     _js="poseRotateLeftUpperLeg3DModel")
        left_upper_leg_z_page.change(None, [left_upper_leg_x_page, left_upper_leg_y_page, left_upper_leg_z_page], None,
                                     _js="poseRotateLeftUpperLeg3DModel")

        left_lower_arm_x_page.change(None, [left_lower_arm_x_page, left_lower_arm_y_page, left_lower_arm_z_page], None, _js="poseRotateLeftLowerArm3DModel")
        left_lower_arm_y_page.change(None, [left_lower_arm_x_page, left_lower_arm_y_page, left_lower_arm_z_page], None, _js="poseRotateLeftLowerArm3DModel")
        left_lower_arm_z_page.change(None, [left_lower_arm_x_page, left_lower_arm_y_page, left_lower_arm_z_page], None, _js="poseRotateLeftLowerArm3DModel")

        right_lower_arm_x_page.change(None, [right_lower_arm_x_page, right_lower_arm_y_page, right_lower_arm_z_page], None, _js="poseRotateRightLowerArm3DModel")
        right_lower_arm_y_page.change(None, [right_lower_arm_x_page, right_lower_arm_y_page, right_lower_arm_z_page], None, _js="poseRotateRightLowerArm3DModel")
        right_lower_arm_z_page.change(None, [right_lower_arm_x_page, right_lower_arm_y_page, right_lower_arm_z_page], None, _js="poseRotateRightLowerArm3DModel")

        left_upper_arm_x_page.change(None, [left_upper_arm_x_page, left_upper_arm_y_page, left_upper_arm_z_page], None, _js="poseRotateLeftUpperArm3DModel")
        left_upper_arm_y_page.change(None, [left_upper_arm_x_page, left_upper_arm_y_page, left_upper_arm_z_page], None, _js="poseRotateLeftUpperArm3DModel")
        left_upper_arm_z_page.change(None, [left_upper_arm_x_page, left_upper_arm_y_page, left_upper_arm_z_page], None, _js="poseRotateLeftUpperArm3DModel")

        right_upper_arm_x_page.change(None, [right_upper_arm_x_page, right_upper_arm_y_page, right_upper_arm_z_page], None, _js="poseRotateRightUpperArm3DModel")
        right_upper_arm_y_page.change(None, [right_upper_arm_x_page, right_upper_arm_y_page, right_upper_arm_z_page], None, _js="poseRotateRightUpperArm3DModel")
        right_upper_arm_z_page.change(None, [right_upper_arm_x_page, right_upper_arm_y_page, right_upper_arm_z_page], None, _js="poseRotateRightUpperArm3DModel")

        neck_x_page.change(None, [neck_x_page, neck_y_page, neck_z_page], None, _js="poseRotateNeck3DModel")
        neck_y_page.change(None, [neck_x_page, neck_y_page, neck_z_page], None, _js="poseRotateNeck3DModel")
        neck_z_page.change(None, [neck_x_page, neck_y_page, neck_z_page], None,
                                  _js="poseRotateNeck3DModel")

        progress_bar.change(None, [progress_bar], None, _js="setCurrentAnimationTime3DModel")
        model_rotate_x_page.change(None, [model_rotate_x_page, model_rotate_y_page, model_rotate_z_page],
                                   None, _js="rotateModel3DModel")
        model_rotate_y_page.change(None, [model_rotate_x_page, model_rotate_y_page, model_rotate_z_page],
                                   None, _js="rotateModel3DModel")
        model_rotate_z_page.change(None, [model_rotate_x_page, model_rotate_y_page, model_rotate_z_page],
                                   None, _js="rotateModel3DModel")

        light_position_x_page.change(None, [light_position_x_page, light_position_y_page, light_position_z_page],
                                     None, _js="moveLight3DModel")
        light_position_y_page.change(None, [light_position_x_page, light_position_y_page, light_position_z_page],
                                     None, _js="moveLight3DModel")
        light_position_z_page.change(None, [light_position_x_page, light_position_y_page, light_position_z_page],
                                     None, _js="moveLight3DModel")
        entry_type.change(None, [entry_type], None, _js="setEntryType3DModel")
        width_page.change(None, [width_page, height_page], None, _js="setCanvasSize3DModel")
        height_page.change(None, [width_page, height_page], None, _js="setCanvasSize3DModel")
        model_scale_page.change(None, [model_scale_page], None, _js="updateModel3DModel")
        has_ground_page.change(None, [has_ground_page], None, _js="setGroundVisible3DModel")
        multi_files_checkbox.change(None, [multi_files_checkbox], None, _js="setMultiFiles3DModel")
        has_ground_grid_page.change(None, [has_ground_grid_page], None, _js="setGroundGridVisible3DModel")
        has_axis_page.change(None, [has_axis_page], None, _js="setAxisVisible3DModel")
        color_page.change(None, [color_page], None, _js="setBGColor3DModel")
        ground_color_page.change(None, [ground_color_page], None, _js="setGroundColor3DModel")
        light_color_page.change(None, [light_color_page], None, _js="setLightColor3DModel")
        play_pause_button.click(None, [], None, _js="playAndPause3DModel")
        stop_button.click(None, [], None, _js="stop3DModel")
        send_t2t.click(None, select_target_index, None, _js="(i) => {sendImage3DModel('txt2img', i)}")
        send_i2i.click(None, select_target_index, None, _js="(i) => {sendImage3DModel('img2img', i)}")
        reset_btn.click(None, [], None, _js="restCanvasAndCamera3DModel")
        upload_button.click(None, None, None, _js="uploadFile3DModel")

    return [(threeDModel_loader, "3D Model Loader", "3dmodel_loador")]


def get_self_extension():
    if '__file__' in globals():
        filepath = __file__
    else:
        import inspect
        filepath = inspect.getfile(lambda: None)
    for ext in extensions.active():
        if ext.path in filepath:
            return ext


def on_ui_settings():
    section = ('3dmodel', "3D Model")
    shared.opts.add_option("threeDmodel_bg_color", shared.OptionInfo(
        "#ffffff", "Canvas Background Color", gr.ColorPicker, {"interactive": True}, section=section))
    shared.opts.add_option("threeDmodel_ground_color", shared.OptionInfo(
        "#ffffff", "Canvas Ground Color", gr.ColorPicker, {"interactive": True}, section=section))
    shared.opts.add_option("threeDmodel_canvas_width", shared.OptionInfo(
        512, "Canvas Width", gr.Slider, {"minimum": 64, "maximum": 2048, "step": 64, "interactive": True},
        section=section))
    shared.opts.add_option("threeDmodel_canvas_height", shared.OptionInfo(
        512, "Canvas Height", gr.Slider, {"minimum": 64, "maximum": 2048, "step": 64, "interactive": True},
        section=section))
    shared.opts.add_option("threeDmodel_has_ground", shared.OptionInfo(
        True, "Show Ground", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("threeDmodel_has_ground_grid", shared.OptionInfo(
        True, "Show Grid", gr.Checkbox, {"interactive": True}, section=section))
    shared.opts.add_option("threeDmodel_has_axis", shared.OptionInfo(
        True, "Show Axis", gr.Checkbox, {"interactive": True}, section=section))


script_callbacks.on_ui_tabs(on_ui_tabs)
script_callbacks.on_ui_settings(on_ui_settings)
