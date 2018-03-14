using System;
using System.Collections.Generic;

namespace MeetupHelper
{
    class Program
    {
        static void Main(string[] args)
        {
            var meetup = new Meetup();

            meetup.Name = "Operation Code";

            meetup.Organizers.Add("James (O)");
            meetup.Organizers.Add("Shirley (O)");

            meetup.Start();
            Console.WriteLine(Environment.NewLine);
            Console.WriteLine("Meetup in progress. Fun stuff is happening and people are learning. Press enter to continue...");
            Console.ReadLine();

            meetup.End();
            Console.WriteLine(Environment.NewLine);
            Console.WriteLine("Meetup has ended. Let's go home. Press enter to continue...");
            Console.ReadLine();
        }

        static List<Attendee> GetAttendees()
        {
            var attendees = new List<Attendee>();
            attendees.Add(new Attendee("Mary (A)", 0));
            attendees.Add(new Attendee("Ben (A)", 0));
            attendees.Add(new Attendee("Levi (A)", 0));
            attendees.Add(new Attendee("Cheryl (A)", 0));
            attendees.Add(new Attendee("William (A)", 0));
            attendees.Add(new Attendee("Evette (A)", 0));
            attendees.Add(new Attendee("Antonio (A)", 0));
            attendees.Add(new Attendee("Jack (A)", 0));
            attendees.Add(new Attendee("Mary (A)", 0));
            attendees.Add(new Attendee("Mary (A)", 0));
            attendees.Add(new Attendee("Mary (A)", 0));
            return attendees;
        }
    }
}
