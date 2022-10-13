def can_build(env, platform):
    return True


def configure(env):
    pass


def get_doc_classes():
    return [
        "RetargetAnimationPlayer",
        "RetargetAnimationTree",
        "RetargetPoseTransporter",
        "RetargetProfile",
        "RetargetProfileAbsoluteAll",
        "RetargetProfileGlobalAll",
        "RetargetProfileLocalAll",
        "RetargetProfileLocalFingersGlobalOthers",
        "RetargetProfileLocalLimbsGlobalOthers",
        "RetargetUtility",
    ]


def get_doc_path():
    return "doc_classes"
