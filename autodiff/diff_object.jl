struct DiffObject <: Number
    f::Tuple{Float64,Float64}
end

import Base: +, -, *, /, ^, convert, promote_rule

+(x::DiffObject, y::DiffObject) = DiffObject(x.f .+ y.f)

-(x::DiffObject, y::DiffObject) = DiffObject(x.f .- y.f)

*(x::DiffObject, y::DiffObject) = DiffObject((x.f[1] * y.f[1], x.f[2] * y.f[1] + x.f[1] * y.f[2]))

/(x::DiffObject, y::DiffObject) = DiffObject((x.f[1] / y.f[1], (y.f[1] * x.f[2] - x.f[1] * y.f[2]) / y.f[1]^2))

^(x::DiffObject, y::DiffObject) = DiffObject((x.f[1]^y.f[1], y.f[1] * x.f[1]^(y.f[1] - 1) * x.f[2] + x.f[1]^y.f[1] * log(x.f[1]) * y.f[2]))

convert(::Type{DiffObject}, x::Real) = DiffObject((x, zero(x)))
promote_rule(::Type{DiffObject}, ::Type{<:Number}) = DiffObject

x = 49

function f(x, y)
    x * y
end

f(DiffObject((3, 1)), 1)

f(DiffObject((3, 1)), 2)

f(1, DiffObject((3, 1)))

f(DiffObject((2, 1)), DiffObject((3, 1)))
