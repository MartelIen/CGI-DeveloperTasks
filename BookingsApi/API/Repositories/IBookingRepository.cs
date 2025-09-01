using System.Collections.Generic;
using BookingsApi.Models;

namespace BookingsApi.Repositories
{
    public interface IBookingRepository
    {
        IEnumerable<Booking> GetAll();
        Booking? GetById(int id);
        Booking Add(Booking booking);
        bool Delete(int id);
    }
}
