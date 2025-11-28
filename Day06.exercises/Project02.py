'''
Event Attendees Tracker

Objective: Track attendees for multiple events using sets.

Features:

Store attendees of Event A and Event B as sets.

Find attendees who attended both events (intersection).

Find attendees who attended either event (union).

Find attendees who attended only one of the events (symmetric difference).

Check if all attendees of Event A are included in Event B (subset check).

Remove a canceled attendee safely using discard().

Add last-minute attendees using add() or update().

Display a sorted list of all attendees.
'''
#Day 06 of Python Learning

event_a = {'Alice', 'Bob', 'Charlie', 'Diana'}
event_b = {'Charlie', 'David', 'Alice', 'Eve'}

both_events = event_a.intersection(event_b)
print(f"Attended both events:{both_events}")

either_event = event_a.union(event_b)
print(f"Attended either event:{either_event}")

only_one_event = event_a.symmetric_difference(event_b)
print(f"Attended only one event:{only_one_event}")

subset_check = event_a.issubset(event_b)
print(f"All Event A attendees in Event B? {subset_check}")

event_a.discard('Diana')

event_b.update(['Frank', 'Grace'])

all_attendees = sorted(event_a.union(event_b))
print(f"Final attendees list:{all_attendees}")
