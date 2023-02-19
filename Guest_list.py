#list of guest for dinner
guest_list = ['aman', 'john', 'scot', 'racheal', 'gorge', 'aslam' ]
print(guest_list)

#personalise invite
for guest in guest_list:
    invite = f"\nHello {guest} ! We are excited to have you with us for Dinner party tonight at Taj."
    print(invite)

#not coming guest
not_coming = 'john'
guest_list.remove(not_coming)
print(f"\n{not_coming.title()}, All the best for your new born baby! We are thrilled to hear. let's catch up next time.")

#updated list list
print(guest_list)

#updated personlised invite
for guest in guest_list:
    invite = f"\nHey {guest}! Let's have a toast for the new born baby of one of our employee Mr.'John'"
    print(invite)

#Change in plan
print(guest_list)
for guest in guest_list:
    invite = f"\nHey {guest}! We have got Couple of more tables on high discount, Let's Invite our college mates."
    print(invite)

#More invites
print(guest_list)
#add guest at first place
guest_list.insert(0, 'steve')
print(guest_list)

#add guest in the middle

guest_list.insert(3, 'Kevin')
print(guest_list)

#add guest in the list at last place
guest_list.append('bala')
print(guest_list)

#Let's Bang
for guest in guest_list:
    invite = f"Hey {guest}! Let's have Reunion Dinner Party tonight at Taj at 10 P.M."
    print(invite)

#inform about availablity
for guest in guest_list:
    invite = f"Hey {guest}! We are regret to inform you that due to over crowd at Taj, We are unable to invite more " \
             f"than two guest. "
    print(invite)

#invite only two guests
guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)

#final invite
for guest in guest_list:
    invite = f"Hey! {guest} We Are finally meeting for dinner at 11 P.M."
    print(invite)

#empty the guest list

del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)
