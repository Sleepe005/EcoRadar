using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Text.Json;

namespace MapInfoAPI.Controllers
{
    [ApiController]
    [Route("/[controller]")]
    public class ExternalFactorsController : ControllerBase
    {
        private readonly ApplicationContext _context;

        public ExternalFactorsController(ApplicationContext context)
        {
            _context = context;
        }

        [HttpGet("GetWind")]
        public async Task<string> GetFactors(int x, int y)
        {
            var square = await _context.ExternalFactors.Select(s => s.X == x && s.Y == y).FirstOrDefaultAsync();
            return JsonSerializer.Serialize(square);
        }
    }
}
