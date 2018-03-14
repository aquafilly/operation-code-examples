namespace MeetupHelper
{
    public class Attendee
    {
        public string Name { get; set; }
        public int MeetupsAttended { get; set; }

        public Attendee(string name, int meetupsAttended)
        {
            Name = name;
            MeetupsAttended = meetupsAttended;
        }
    }
}
