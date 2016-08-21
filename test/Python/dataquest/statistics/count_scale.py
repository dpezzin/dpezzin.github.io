#!/usr/bin/env python
# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]


# Assign the number that indicates its position on the scale to each survey response ("none" is 0, and so on).
# Compute the average value of all the survey responses, and assign it to average_smoking.
survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response) for response in survey_responses]
average_smoking = sum(survey_numbers) / len(survey_numbers)