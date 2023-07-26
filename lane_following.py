import numpy as np


def get_lane_center(lanes: np.ndarray):
    """
    Takes a list of lanes and returns the center of the closest lane and its slope.

        Parameters:
            lanes (np.ndarray): The list of lanes to process.

        Returns:
            center_intercept (float): The horizontal intercept of the center of the closest lane.
            center_slope (float): The slope of the closest lane.
    """

    pass


def recommend_direction(center: float, slope: float):
    """
    Takes the center of the closest lane and its slope as inputs and returns a direction.

        Parameters:
            center (float): The center of the closest lane.
            slope (float): The slope of the closest lane.

        Returns:
            direction (str): left, right, forward
    """

    pass
