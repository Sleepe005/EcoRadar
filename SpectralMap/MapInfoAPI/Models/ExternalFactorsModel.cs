namespace MapInfoAPI.Models
{
    public class ExternalFactorsModel
    {
        private int x;
        private int y;
        private int windSpeed;
        private int windDirection;

        public int X { get => x; set => x = value; }
        public int Y { get => y; set => y = value; }
        public int WindSpeed { get => windSpeed; set => windSpeed = value; }
        public int WindDirection { get => windDirection; set => windDirection = value; }
    }
}
