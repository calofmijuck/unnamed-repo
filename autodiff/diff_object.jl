struct DiffObject <: Number
    f::Number
    df::Number

    DiffObject(f::Number, df::Number) = new(f, df)
    DiffObject(f::Number) = new(f, one(f))
end

import Base: +, -, *, /, ^, sin, cos, tan, exp, log, convert, promote_rule

+(x::DiffObject, y::DiffObject) = DiffObject(x.f + y.f, x.df + y.df)

-(x::DiffObject, y::DiffObject) = DiffObject(x.f - y.f, x.df - y.df)

*(x::DiffObject, y::DiffObject) = DiffObject(x.f * y.f, x.df * y.f + x.f * y.df)

/(x::DiffObject, y::DiffObject) = DiffObject(x.f / y.f, (x.df * y.f - x.f * y.df) / y.f^2)

^(x::DiffObject, y::DiffObject) = DiffObject(x.f^y.f, y.f * x.f^(y.f - 1) * x.df + x.f^y.f * log(x.f) * y.df)

sin(x::DiffObject) = DiffObject(sin(x.f), x.df * cos(x.f))

cos(x::DiffObject) = DiffObject(cos(x.f), -x.df * sin(x.f))

tan(x::DiffObject) = DiffObject(tan(x.f), x.df * sec(x.f)^2)

exp(x::DiffObject) = DiffObject(exp(x.f), x.df * exp(x.f))

log(x::DiffObject) = DiffObject(log(x.f), x.df / x.f)

convert(::Type{DiffObject}, x::Real) = DiffObject(x, zero(x))

promote_rule(::Type{DiffObject}, ::Type{<:Number}) = DiffObject

x = 49

function f(x, y)
    x * y
end

f(DiffObject((3, 1)), 1)

f(DiffObject((3, 1)), 2)

f(1, DiffObject((3, 1)))

f(DiffObject((2, 1)), DiffObject((3, 1)))
