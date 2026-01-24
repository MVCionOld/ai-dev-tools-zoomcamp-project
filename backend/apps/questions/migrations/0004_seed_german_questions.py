"""Seed German mock questions with explanations."""
from __future__ import annotations

from django.db import migrations


GERMAN_QUESTIONS = [
    {
        "topic": "right_of_way",
        "difficulty": "beginner",
        "text": "At an unmarked intersection of equal priority, who has right of way?",
        "options": [
            {"key": "A", "text": "Vehicle from the left"},
            {"key": "B", "text": "Vehicle from the right"},
            {"key": "C", "text": "Vehicle going straight"},
            {"key": "D", "text": "Vehicle that arrived first"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "In Germany, the right-before-left rule applies at equal intersections.",
            "B": "Correct: right-before-left gives priority to the vehicle from the right.",
            "C": "Going straight does not override right-before-left at equal intersections.",
            "D": "Arrival order does not replace the right-before-left rule.",
        },
    },
    {
        "topic": "road_signs",
        "difficulty": "beginner",
        "text": "What does a red octagonal STOP sign require?",
        "options": [
            {"key": "A", "text": "Stop completely and yield"},
            {"key": "B", "text": "Slow down and continue if clear"},
            {"key": "C", "text": "Stop only if pedestrians"},
            {"key": "D", "text": "Honk and proceed"},
        ],
        "correct_answer": "A",
        "explanations": {
            "A": "Correct: STOP requires a full stop and yielding to cross traffic.",
            "B": "Slowing without a full stop is insufficient for a STOP sign.",
            "C": "The stop applies regardless of pedestrians.",
            "D": "Horn use is not a substitute for stopping.",
        },
    },
    {
        "topic": "speed_limits",
        "difficulty": "beginner",
        "text": "Default speed limit in built-up areas in Germany is:",
        "options": [
            {"key": "A", "text": "30 km/h"},
            {"key": "B", "text": "50 km/h"},
            {"key": "C", "text": "60 km/h"},
            {"key": "D", "text": "70 km/h"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "30 km/h applies only where posted (Tempo 30 zones).",
            "B": "Correct: 50 km/h is the default in built-up areas unless signed otherwise.",
            "C": "60 km/h is above the default and only applies if posted.",
            "D": "70 km/h is not the default for built-up areas.",
        },
    },
    {
        "topic": "speed_limits",
        "difficulty": "intermediate",
        "text": "On rural roads (outside built-up areas), the default limit for cars is:",
        "options": [
            {"key": "A", "text": "80 km/h"},
            {"key": "B", "text": "90 km/h"},
            {"key": "C", "text": "100 km/h"},
            {"key": "D", "text": "120 km/h"},
        ],
        "correct_answer": "C",
        "explanations": {
            "A": "80 km/h may apply to specific vehicles or conditions, not the default for cars.",
            "B": "90 km/h is not the default for cars on rural roads in Germany.",
            "C": "Correct: 100 km/h is the default for cars outside built-up areas.",
            "D": "120 km/h is not the default on rural roads.",
        },
    },
    {
        "topic": "autobahn",
        "difficulty": "intermediate",
        "text": "What is the general rule for speed on the Autobahn?",
        "options": [
            {"key": "A", "text": "No limit everywhere"},
            {"key": "B", "text": "Recommended 130 km/h where no limit is posted"},
            {"key": "C", "text": "Fixed 130 km/h limit"},
            {"key": "D", "text": "Fixed 120 km/h limit"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Many sections have posted limits; it is not unlimited everywhere.",
            "B": "Correct: 130 km/h is a recommended speed where no limit is posted.",
            "C": "130 km/h is not a fixed legal limit everywhere.",
            "D": "120 km/h is not the general Autobahn rule.",
        },
    },
    {
        "topic": "seat_belts",
        "difficulty": "beginner",
        "text": "Seat belts in Germany are:",
        "options": [
            {"key": "A", "text": "Optional in city traffic"},
            {"key": "B", "text": "Required for all occupants"},
            {"key": "C", "text": "Required only for front seats"},
            {"key": "D", "text": "Required only on highways"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Seat belts are mandatory regardless of location.",
            "B": "Correct: all occupants must wear seat belts.",
            "C": "Rear occupants are also required to wear belts.",
            "D": "The requirement applies everywhere, not just highways.",
        },
    },
    {
        "topic": "phone_use",
        "difficulty": "beginner",
        "text": "Using a handheld mobile phone while driving is:",
        "options": [
            {"key": "A", "text": "Allowed at traffic lights"},
            {"key": "B", "text": "Allowed if using speaker"},
            {"key": "C", "text": "Prohibited"},
            {"key": "D", "text": "Allowed for navigation"},
        ],
        "correct_answer": "C",
        "explanations": {
            "A": "Handheld use is prohibited even while stopped in traffic.",
            "B": "Speaker use is allowed only if hands-free; handheld is still banned.",
            "C": "Correct: handheld phone use while driving is prohibited.",
            "D": "Navigation is allowed only if hands-free; handheld use is banned.",
        },
    },
    {
        "topic": "parking",
        "difficulty": "beginner",
        "text": "How far from a pedestrian crossing must you park?",
        "options": [
            {"key": "A", "text": "3 meters"},
            {"key": "B", "text": "5 meters"},
            {"key": "C", "text": "10 meters"},
            {"key": "D", "text": "15 meters"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "3 meters is too close; visibility is restricted.",
            "B": "Correct: 5 meters is the minimum distance in Germany.",
            "C": "10 meters is not required for pedestrian crossings.",
            "D": "15 meters is not the legal requirement for crossings.",
        },
    },
    {
        "topic": "rail_crossing",
        "difficulty": "beginner",
        "text": "At a level crossing with flashing red lights, you must:",
        "options": [
            {"key": "A", "text": "Continue if no train is visible"},
            {"key": "B", "text": "Stop and wait"},
            {"key": "C", "text": "Proceed quickly"},
            {"key": "D", "text": "Honk and cross"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Flashing red lights mean stop regardless of visibility.",
            "B": "Correct: you must stop and wait.",
            "C": "Speeding up is unsafe and illegal.",
            "D": "Horns do not grant priority at crossings.",
        },
    },
    {
        "topic": "emergency_vehicles",
        "difficulty": "intermediate",
        "text": "When an emergency vehicle approaches with siren and blue light, you should:",
        "options": [
            {"key": "A", "text": "Stop immediately where you are"},
            {"key": "B", "text": "Move to the right and slow down/stop"},
            {"key": "C", "text": "Accelerate to clear the area"},
            {"key": "D", "text": "Maintain speed"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Stopping in place can block the emergency path.",
            "B": "Correct: create a clear path by moving right and stopping if needed.",
            "C": "Accelerating can be unsafe and illegal.",
            "D": "You must yield and clear the path.",
        },
    },
    {
        "topic": "alcohol",
        "difficulty": "intermediate",
        "text": "For most drivers in Germany, the legal BAC limit is:",
        "options": [
            {"key": "A", "text": "0.0‰"},
            {"key": "B", "text": "0.3‰"},
            {"key": "C", "text": "0.5‰"},
            {"key": "D", "text": "0.8‰"},
        ],
        "correct_answer": "C",
        "explanations": {
            "A": "0.0‰ applies to novice/professional drivers, not all drivers.",
            "B": "0.3‰ can already be punishable with impairment, but limit is higher.",
            "C": "Correct: 0.5‰ is the general legal limit.",
            "D": "0.8‰ exceeds the legal limit.",
        },
    },
    {
        "topic": "priority_signs",
        "difficulty": "beginner",
        "text": "A yellow diamond sign in Germany means:",
        "options": [
            {"key": "A", "text": "Give way"},
            {"key": "B", "text": "You are on a priority road"},
            {"key": "C", "text": "Stop"},
            {"key": "D", "text": "No entry"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Give way is an inverted triangle sign.",
            "B": "Correct: yellow diamond indicates a priority road.",
            "C": "Stop is a red octagon.",
            "D": "No entry is a red circle with a white bar.",
        },
    },
    {
        "topic": "overtaking",
        "difficulty": "intermediate",
        "text": "Overtaking on the right on Autobahn is:",
        "options": [
            {"key": "A", "text": "Allowed if traffic is slow"},
            {"key": "B", "text": "Allowed only at night"},
            {"key": "C", "text": "Generally prohibited"},
            {"key": "D", "text": "Required in heavy traffic"},
        ],
        "correct_answer": "C",
        "explanations": {
            "A": "Right-side overtaking is generally prohibited.",
            "B": "Nighttime does not change the rule.",
            "C": "Correct: overtaking should be on the left.",
            "D": "There is no requirement to overtake on the right.",
        },
    },
    {
        "topic": "roundabouts",
        "difficulty": "beginner",
        "text": "In a German roundabout with yield signs, who has priority?",
        "options": [
            {"key": "A", "text": "Vehicles entering"},
            {"key": "B", "text": "Vehicles inside the roundabout"},
            {"key": "C", "text": "Vehicles on the right"},
            {"key": "D", "text": "Pedestrians"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Entering vehicles must yield.",
            "B": "Correct: traffic already in the roundabout has priority.",
            "C": "Right-before-left does not apply with yield signs.",
            "D": "Pedestrians have separate crossings, not priority inside.",
        },
    },
    {
        "topic": "lighting",
        "difficulty": "beginner",
        "text": "When should you use dipped headlights in Germany?",
        "options": [
            {"key": "A", "text": "Only at night"},
            {"key": "B", "text": "Only in tunnels"},
            {"key": "C", "text": "At night and in poor visibility"},
            {"key": "D", "text": "Only on highways"},
        ],
        "correct_answer": "C",
        "explanations": {
            "A": "Dipped headlights are also required in poor visibility.",
            "B": "Tunnels are one case, but not the only one.",
            "C": "Correct: use dipped headlights at night and in poor visibility.",
            "D": "Headlight use is not restricted to highways.",
        },
    },
    {
        "topic": "environment",
        "difficulty": "beginner",
        "text": "When waiting for more than a brief moment, you should:",
        "options": [
            {"key": "A", "text": "Keep the engine running"},
            {"key": "B", "text": "Turn off the engine"},
            {"key": "C", "text": "Rev the engine"},
            {"key": "D", "text": "Open the hood"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Idling for long periods is discouraged by environmental rules.",
            "B": "Correct: turn off the engine when waiting for a longer time.",
            "C": "Revving wastes fuel and increases emissions.",
            "D": "Opening the hood is not required.",
        },
    },
    {
        "topic": "children",
        "difficulty": "beginner",
        "text": "Children under 12 or below 150 cm must:",
        "options": [
            {"key": "A", "text": "Sit in front seat without booster"},
            {"key": "B", "text": "Use an appropriate child restraint"},
            {"key": "C", "text": "Sit on an adult's lap"},
            {"key": "D", "text": "Stand in the back seat"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Child restraints are mandatory for younger/smaller children.",
            "B": "Correct: child restraints are required.",
            "C": "Holding a child is unsafe and illegal.",
            "D": "Standing in a vehicle is unsafe and illegal.",
        },
    },
    {
        "topic": "priority_pedestrian",
        "difficulty": "beginner",
        "text": "At a pedestrian crossing (zebra), drivers must:",
        "options": [
            {"key": "A", "text": "Accelerate to pass before pedestrians"},
            {"key": "B", "text": "Yield and stop if necessary"},
            {"key": "C", "text": "Honk to warn"},
            {"key": "D", "text": "Only yield to children"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Pedestrians have priority; accelerating is unsafe and illegal.",
            "B": "Correct: yield and stop when needed.",
            "C": "Horn use does not replace yielding.",
            "D": "Priority applies to all pedestrians.",
        },
    },
    {
        "topic": "lane_discipline",
        "difficulty": "intermediate",
        "text": "On highways, you should:",
        "options": [
            {"key": "A", "text": "Keep right except when overtaking"},
            {"key": "B", "text": "Drive in the middle lane"},
            {"key": "C", "text": "Use left lane for cruising"},
            {"key": "D", "text": "Change lanes frequently"},
        ],
        "correct_answer": "A",
        "explanations": {
            "A": "Correct: keep right unless overtaking.",
            "B": "Middle lane cruising is discouraged.",
            "C": "Left lane is for overtaking, not cruising.",
            "D": "Frequent lane changes increase risk.",
        },
    },
    {
        "topic": "winter_tires",
        "difficulty": "intermediate",
        "text": "Winter tires in Germany are:",
        "options": [
            {"key": "A", "text": "Required in all winter months"},
            {"key": "B", "text": "Required in wintry conditions"},
            {"key": "C", "text": "Never required"},
            {"key": "D", "text": "Required only in snow"},
        ],
        "correct_answer": "B",
        "explanations": {
            "A": "Requirement is condition-based, not month-based.",
            "B": "Correct: winter tires are required in wintry conditions.",
            "C": "Winter tires can be mandatory.",
            "D": "It is broader than just snow (ice, slush).",
        },
    },
]


def seed_german_questions(apps, schema_editor) -> None:
    """Seed German mock questions with incorrect-choice explanations."""
    Jurisdiction = apps.get_model("jurisdictions", "Jurisdiction")
    Question = apps.get_model("questions", "Question")

    jurisdiction = Jurisdiction.objects.filter(code="DE").first()
    if not jurisdiction:
        return

    Question.objects.filter(jurisdiction=jurisdiction, source="seed").delete()

    questions = []
    for entry in GERMAN_QUESTIONS:
        questions.append(
            Question(
                jurisdiction=jurisdiction,
                type="multiple_choice",
                difficulty=entry["difficulty"],
                topic=entry["topic"],
                content_json={
                    "text": entry["text"],
                    "image_url": None,
                    "options": entry["options"],
                    "option_explanations": entry["explanations"],
                },
                correct_answer=entry["correct_answer"],
                source="seed",
                validated=True,
                explanation_cache=None,
            )
        )

    Question.objects.bulk_create(questions)


def unseed_german_questions(apps, schema_editor) -> None:
    """Remove seeded German mock questions."""
    Jurisdiction = apps.get_model("jurisdictions", "Jurisdiction")
    Question = apps.get_model("questions", "Question")

    jurisdiction = Jurisdiction.objects.filter(code="DE").first()
    if not jurisdiction:
        return

    Question.objects.filter(jurisdiction=jurisdiction, source="seed").delete()


class Migration(migrations.Migration):
    """Seed German mock questions with explanations."""

    dependencies = [
        ("questions", "0003_rename_question_indexes"),
        ("jurisdictions", "0002_seed_jurisdictions"),
    ]

    operations = [
        migrations.RunPython(seed_german_questions, reverse_code=unseed_german_questions),
    ]