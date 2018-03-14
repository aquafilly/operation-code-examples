using System;
using System.Collections.Generic;
using System.Text;

namespace MeetupHelper
{
    public class Meetup
    {
        public List<string> Organizers { get; set; }
        public List<Attendee> Attendees { get; set; }
        public string Name { get; set; }

        public Meetup()
        {
            Organizers = new List<string>();
            Attendees = new List<Attendee>();
        }

        public void Start()
        {
            foreach(var organizer in Organizers)
            {
                foreach(var attendee in Attendees)
                {
                    Console.WriteLine($"{organizer} greets {attendee} to {Name}");
                }
            }
        }

        public void End()
        {
            foreach (var organizer in Organizers)
            {
                foreach (var attendee in Attendees)
                {
                    Console.WriteLine($"{organizer} thanks {attendee} for coming and welcomes them back to the next {Name} meetup.");
                }
            }
        }
    }
}
