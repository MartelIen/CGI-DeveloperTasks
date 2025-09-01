using BookingsApi.Models;
using BookingsApi.Repositories;
using BookingsApi.Services;

namespace BookingsApi.Services
{
    public class BookingService : IBookingService
    {        
        private readonly IBookingRepository _repo;

        public BookingService(IBookingRepository repo)
        {
            _repo = repo;
        }

        public IEnumerable<Booking> GetAll() => _repo.GetAll();
        
        public Booking? GetById(int id) => _repo.GetById(id);

        /// <summary>
        /// Returnerar true om tidsintervallet krockar med befintlig bokning
        /// </summary>
        public bool HasOverlap(int roomId, DateTime from, DateTime to)
        {
            return _repo.GetAll().Any(b =>
            b.RoomId == roomId && 
            from < b.To &&              // new booking starts before existing booking ends
            b.From < to);               // existing booking starts before new booking ends
        }

        public Booking Create(Booking booking)
        {        
            if (HasOverlap(booking.RoomId, booking.From, booking.To))
                throw new InvalidOperationException("Booking overlaps");

            return _repo.Add(booking);
        }

        public bool Cancel(int id) => _repo.Delete(id);
    }
}
