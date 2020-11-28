#include <iostream>
#include <vector>

#ifndef LINALG_VECTOR_H
#define LINALG_VECTOR_H

/*
    Naive implementation of Vectors.
*/

template <typename T>
class Vector
{
private:
    std::vector<T> m_data;

public:
    // creates a Vector with a given dimension
    Vector(int dim)
    {
        m_data.resize(dim, T());
    }

    // create a Vector and initialize it to a value
    Vector(int dim, T val)
    {
        m_data.resize(dim, val);
    }

    // creates a Vector from a given std::vector
    Vector(const std::vector<T> data)
    {
        m_data.resize(data.size());
        std::copy(data.begin(), data.end(), m_data.begin());
    }

    // creates a Vector from a given Vector
    Vector(const Vector<T> &other) : Vector(other.to_std_vector())
    {
    }

    // convert to std::vector
    std::vector<T> to_std_vector() const
    {
        return m_data;
    }

    // dimension of Vector
    size_t size() const
    {
        return m_data.size();
    }

    // indexing elements
    T &operator[](size_t idx)
    {
        return m_data[idx];
    }

    const T &operator[](size_t idx) const
    {
        return m_data[idx];
    }

    // assignment
    Vector<T> &operator=(const Vector<T> &other)
    {
        std::vector<T> data = other.to_std_vector();
        m_data.resize(data.size());
        std::copy(data.begin(), data.end(), m_data.begin());
        return *this;
    }
};

// addition
template <typename T>
Vector<T> operator+(const Vector<T> curr, const Vector<T> &other)
{
    // size check
    if (curr.size() != other.size())
    {
        // error!
    }
    std::vector<T> ret(curr.size());
    for (int i = 0; i < (int)ret.size(); ++i)
    {
        ret[i] = curr[i] + other[i];
    }
    return Vector<T>(ret);
}

// subtraction
template <typename T>
Vector<T> operator-(const Vector<T> curr, const Vector<T> &other)
{
    // size check
    if (curr.size() != other.size())
    {
        // error!
    }
    std::vector<T> ret(curr.size());
    for (int i = 0; i < (int)ret.size(); ++i)
    {
        ret[i] = curr[i] - other[i];
    }
    return Vector<T>(ret);
}

// constant multiplication
template <typename T>
Vector<T> operator*(const T &val, const Vector<T> &other)
{
    std::vector<T> ret(other.size());
    for (int i = 0; i < (int)ret.size(); ++i)
    {
        ret[i] = val * other[i];
    }
    return Vector<T>(ret);
}

// comparing two Vectors
template <typename T>
bool operator==(const Vector<T> curr, const Vector<T> other)
{
    // size check
    if (curr.size() != other.size())
    {
        return false;
    }
    for (int i = 0; i < (int)curr.size(); ++i)
    {
        if (curr[i] != other[i])
        {
            return false;
        }
    }
    return true;
}

template <typename T>
std::ostream &operator<<(std::ostream &sout, const Vector<T> vec)
{
    sout << "(";
    for (int i = 0; i < (int)vec.size(); ++i)
    {
        sout << vec[i];
        if (i != (int)vec.size() - 1)
        {
            sout << ", ";
        }
    }
    sout << ")";
    return sout;
}

#endif
